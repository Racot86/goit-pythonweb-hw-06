from sqlalchemy import func, desc, Float
from sqlalchemy.orm import Session
from models import Student, Grade, Subject, Teacher, Group

# 1. Топ-5 студентів із найвищим середнім балом

def select_1(session: Session):
    result = (
        session.query(Student.name, func.avg(Grade.value).label("avg_grade"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return [(name, round(avg, 2)) for name, avg in result]


# 2. Студент із найвищим середнім балом з певного предмета

def select_2(session: Session, subject_id: int):
    result = (
        session.query(Student.name, func.avg(Grade.value).label("avg_grade"))
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .first()
    )
    if result:
        return (result[0], round(result[1], 2))
    return None


# 3. Середній бал у групах з певного предмета

def select_3(session: Session, subject_id: int):
    result = (
        session.query(Group.name, func.avg(Grade.value).label("avg_grade"))
        .select_from(Group)
        .join(Group.students)
        .join(Student.grades)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )
    return [(name, round(avg, 2)) for name, avg in result]


# 4. Середній бал на потоці (всі оцінки)

def select_4(session: Session):
    avg = session.query(func.avg(Grade.value)).scalar()
    return round(avg, 2) if avg else None


# 5. Які курси читає певний викладач

def select_5(session: Session, teacher_id: int):
    result = (
        session.query(Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )
    return result


# 6. Список студентів у певній групі

def select_6(session: Session, group_id: int):
    result = session.query(Student.name).filter(Student.group_id == group_id).all()
    return result


# 7. Оцінки студентів у групі з певного предмета

def select_7(session: Session, group_id: int, subject_id: int):
    result = (
        session.query(Student.name, Grade.value)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )
    return result


# 8. Середній бал, який ставить певний викладач зі своїх предметів

def select_8(session: Session, teacher_id: int):
    result = (
        session.query(func.avg(Grade.value))
        .join(Subject)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )
    return round(result, 2) if result else None


# 9. Курси, які відвідує певний студент

def select_9(session: Session, student_id: int):
    result = (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )
    return result


# 10. Курси, які певному студенту читає певний викладач

def select_10(session: Session, student_id: int, teacher_id: int):
    result = (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .filter(Subject.teacher_id == teacher_id)
        .distinct()
        .all()
    )
    return result
