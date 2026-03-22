from models import Student


def test_add_student(db_session):
    """Тест добавления студента."""
    new_student = Student(name="John Doe", email="john.doe@example.com")
    db_session.add(new_student)
    db_session.flush()

    assert new_student.id is not None

    student_from_db = db_session.get(Student, new_student.id)
    assert student_from_db.name == "John Doe"
    assert student_from_db.email == "john.doe@example.com"


def test_update_student(db_session):
    """Тест изменения студента."""
    student = Student(name="Jane Doe", email="jane@example.com")
    db_session.add(student)
    db_session.flush()

    student.name = "Jane Smith"
    db_session.flush()

    updated = db_session.get(Student, student.id)
    assert updated.name == "Jane Smith"
    assert updated.email == "jane@example.com"


def test_delete_student(db_session):
    """Тест удаления студента."""
    student = Student(name="To Delete", email="delete@example.com")
    db_session.add(student)
    db_session.flush()
    student_id = student.id

    db_session.delete(student)
    db_session.flush()

    deleted = db_session.get(Student, student_id)
    assert deleted is None
