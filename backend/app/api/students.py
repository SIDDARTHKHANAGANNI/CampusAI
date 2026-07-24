from backend.app.schemas.student import (
    StudentCreate,
    StudentResponse,
    StudentProfileResponse
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# @router.post("/", response_model=StudentResponse, status_code=201)
# def create_student(
#     student: StudentCreate,
#     db: Session = Depends(get_db)
# ):
#     existing_student = (
#         db.query(Student)
#         .filter(Student.email == student.email)
#         .first()
#     )

#     if existing_student:
#         raise HTTPException(
#             status_code=400,
#             detail="A student with this email already exists"
#         )

#     new_student = Student(**student.model_dump())

#     db.add(new_student)
#     db.commit()
#     db.refresh(new_student)

#     return new_student
# @router.get("/", response_model=list[StudentResponse])
# def get_all_students(db: Session = Depends(get_db)):
#     students = db.query(Student).all()
#     return students


@router.get(
    "/me/profile",
    response_model=StudentProfileResponse
)
def get_my_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.user_id == current_user.id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    return student
@router.post(
    "/me/profile",
    response_model=StudentResponse,
    status_code=201
)
def create_my_profile(
    student_data: StudentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Check if this user already owns a student profile
    existing_profile = db.query(Student).filter(
        Student.user_id == current_user.id
    ).first()

    if existing_profile:
        raise HTTPException(
            status_code=400,
            detail="Student profile already exists"
        )

    new_student = Student(
        user_id=current_user.id,
        **student_data.model_dump()
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student
@router.put(
    "/me/profile",
    response_model=StudentResponse
)
def update_my_profile(
    student_data: StudentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.user_id == current_user.id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    for key, value in student_data.model_dump().items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return student


@router.get(
    "/{student_id}/profile",
    response_model=StudentProfileResponse
)
def get_student_profile(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

# @router.get("/{student_id}", response_model=StudentResponse)
# def get_student(student_id: int, db: Session = Depends(get_db)):
#     student = (
#         db.query(Student)
#         .filter(Student.id == student_id)
#         .first()
#     )

#     if not student:
#         raise HTTPException(
#             status_code=404,
#             detail="Student not found"
#         )

#     return student


# @router.put("/{student_id}", response_model=StudentResponse)
# def update_student(
#     student_id: int,
#     student_data: StudentCreate,
#     db: Session = Depends(get_db)
# ):
#     student = (
#         db.query(Student)
#         .filter(Student.id == student_id)
#         .first()
#     )

#     if not student:
#         raise HTTPException(
#             status_code=404,
#             detail="Student not found"
#         )

#     for key, value in student_data.model_dump().items():
#         setattr(student, key, value)

#     db.commit()
#     db.refresh(student)

#     return student


# @router.delete("/{student_id}")
# def delete_student(student_id: int, db: Session = Depends(get_db)):
#     student = (
#         db.query(Student)
#         .filter(Student.id == student_id)
#         .first()
#     )

#     if not student:
#         raise HTTPException(
#             status_code=404,
#             detail="Student not found"
#         )

#     db.delete(student)
#     db.commit()

#     return {
#         "message": "Student deleted successfully"
#     }