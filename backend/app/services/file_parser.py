import fitz
import io


def extract_text_from_file(file_bytes: bytes, filename: str) -> str:
    if filename.lower().endswith(".pdf"):
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        return " ".join(page.get_text() for page in doc)
    elif filename.lower().endswith(".docx"):
        import docx
        d = docx.Document(io.BytesIO(file_bytes))
        return " ".join(p.text for p in d.paragraphs)
    raise ValueError("Unsupported file type. Use PDF or DOCX.")