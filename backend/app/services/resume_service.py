import fitz
import re
import json
import os

CORE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "core")

with open(os.path.join(CORE_DIR, "skills_taxonomy.json")) as f:
    TAXONOMY = json.load(f)
ALL_SKILLS = list(set(sum(TAXONOMY.values(), [])))

with open(os.path.join(CORE_DIR, "jd_templates.json")) as f:
    JD_TEMPLATES = json.load(f)


def extract_text(file_bytes: bytes, filename: str) -> str:
    if filename.endswith(".pdf"):
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        return " ".join(page.get_text() for page in doc)
    elif filename.endswith(".docx"):
        import docx
        import io
        d = docx.Document(io.BytesIO(file_bytes))
        return " ".join(p.text for p in d.paragraphs)
    raise ValueError("Unsupported file type")


def detect_sections(text: str) -> dict:
    sections = ["education", "skills", "projects", "experience", "certifications"]
    return {s: bool(re.search(rf"\b{s}\b", text, re.IGNORECASE)) for s in sections}


def extract_skills(text: str) -> list:
    text_lower = text.lower()
    return list(set(s for s in ALL_SKILLS if s.lower() in text_lower))


def missing_skills(extracted: list, target_role: str) -> list:
    required = JD_TEMPLATES.get(target_role, [])
    return [s for s in required if s not in extracted]


def ats_score(text: str, sections: dict) -> float:
    score = 40 if len(text) > 500 else 20
    score += sum(12 for v in sections.values() if v)
    return min(score, 100)


def compute_resume_score(sections: dict, extracted: list, missing: list, ats: float) -> float:
    section_score = sum(sections.values()) / len(sections) * 30
    skill_score = min(len(extracted) / 10, 1) * 30
    gap_penalty = min(len(missing) * 3, 20)
    ats_component = ats * 0.2
    return round(section_score + skill_score + ats_component - gap_penalty, 1)


def generate_suggestions(sections: dict, missing: list, text: str) -> list:
    tips = []
    if not sections.get("projects"):
        tips.append("Add a Projects section")
    if not sections.get("experience"):
        tips.append("Add Experience or Internship section")
    if missing:
        tips.append(f"Learn/add: {', '.join(missing[:3])}")
    if not re.search(r"\d+%|\d+x|\$\d+", text):
        tips.append("Add quantified achievements (e.g. 'improved X by 20%')")
    return tips


def analyze_resume(file_bytes: bytes, filename: str, target_role: str) -> dict:
    text = extract_text(file_bytes, filename)
    sections = detect_sections(text)
    extracted = extract_skills(text)
    missing = missing_skills(extracted, target_role)
    ats = ats_score(text, sections)
    score = compute_resume_score(sections, extracted, missing, ats)
    suggestions = generate_suggestions(sections, missing, text)
    return {
        "score": score,
        "ats_score": ats,
        "extracted_skills": extracted,
        "missing_skills": missing,
        "sections_detected": sections,
        "suggestions": suggestions,
        "raw_text": text,
    }