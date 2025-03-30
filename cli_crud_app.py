import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Teacher, Group, Student, Subject, Grade

DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

# TEACHER CRUD

def create_teacher(session, name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    print(f"Teacher '{name}' created with id={teacher.id}")

def list_teachers(session):
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"{teacher.id}: {teacher.name}")

def update_teacher(session, id, name):
    teacher = session.get(Teacher, id)
    if teacher:
        teacher.name = name
        session.commit()
        print(f"Teacher with id={id} updated to '{name}'")
    else:
        print(f"Teacher with id={id} not found")

def remove_teacher(session, id):
    teacher = session.get(Teacher, id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher with id={id} deleted")
    else:
        print(f"Teacher with id={id} not found")

# GROUP CRUD

def create_group(session, name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    print(f"Group '{name}' created with id={group.id}")

def list_groups(session):
    groups = session.query(Group).all()
    for group in groups:
        print(f"{group.id}: {group.name}")

def update_group(session, id, name):
    group = session.get(Group, id)
    if group:
        group.name = name
        session.commit()
        print(f"Group with id={id} updated to '{name}'")
    else:
        print(f"Group with id={id} not found")

def remove_group(session, id):
    group = session.get(Group, id)
    if group:
        session.delete(group)
        session.commit()
        print(f"Group with id={id} deleted")
    else:
        print(f"Group with id={id} not found")

# STUDENT CRUD

def create_student(session, name, group_id):
    student = Student(name=name, group_id=group_id)
    session.add(student)
    session.commit()
    print(f"Student '{name}' created with id={student.id}")

def list_students(session):
    students = session.query(Student).all()
    for student in students:
        print(f"{student.id}: {student.name} (Group {student.group_id})")

def update_student(session, id, name):
    student = session.get(Student, id)
    if student:
        student.name = name
        session.commit()
        print(f"Student with id={id} updated to '{name}'")
    else:
        print(f"Student with id={id} not found")

def remove_student(session, id):
    student = session.get(Student, id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Student with id={id} deleted")
    else:
        print(f"Student with id={id} not found")

# SUBJECT CRUD

def create_subject(session, name, teacher_id):
    subject = Subject(name=name, teacher_id=teacher_id)
    session.add(subject)
    session.commit()
    print(f"Subject '{name}' created with id={subject.id}")

def list_subjects(session):
    subjects = session.query(Subject).all()
    for subject in subjects:
        print(f"{subject.id}: {subject.name} (Teacher {subject.teacher_id})")

def update_subject(session, id, name):
    subject = session.get(Subject, id)
    if subject:
        subject.name = name
        session.commit()
        print(f"Subject with id={id} updated to '{name}'")
    else:
        print(f"Subject with id={id} not found")

def remove_subject(session, id):
    subject = session.get(Subject, id)
    if subject:
        session.delete(subject)
        session.commit()
        print(f"Subject with id={id} deleted")
    else:
        print(f"Subject with id={id} not found")

# GRADE CRUD

def create_grade(session, value, student_id, subject_id):
    from datetime import date
    grade = Grade(value=value, date=date.today(), student_id=student_id, subject_id=subject_id)
    session.add(grade)
    session.commit()
    print(f"Grade {value} added for Student {student_id} in Subject {subject_id}")

def list_grades(session):
    grades = session.query(Grade).all()
    for grade in grades:
        print(f"{grade.id}: {grade.value} on {grade.date} (Student {grade.student_id}, Subject {grade.subject_id})")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"], required=True)
    parser.add_argument("-m", "--model", choices=["Teacher", "Group", "Student", "Subject", "Grade"], required=True)
    parser.add_argument("--id", type=int, help="ID of the object to update or remove")
    parser.add_argument("-n", "--name", help="Name for create or update")
    parser.add_argument("--group_id", type=int, help="Group ID for student")
    parser.add_argument("--teacher_id", type=int, help="Teacher ID for subject")
    parser.add_argument("--student_id", type=int, help="Student ID for grade")
    parser.add_argument("--subject_id", type=int, help="Subject ID for grade")
    parser.add_argument("--value", type=float, help="Grade value")

    args = parser.parse_args()
    session = Session(bind=engine)

    match (args.action, args.model):
        case ("create", "Teacher"):
            create_teacher(session, args.name)
        case ("list", "Teacher"):
            list_teachers(session)
        case ("update", "Teacher"):
            update_teacher(session, args.id, args.name)
        case ("remove", "Teacher"):
            remove_teacher(session, args.id)

        case ("create", "Group"):
            create_group(session, args.name)
        case ("list", "Group"):
            list_groups(session)
        case ("update", "Group"):
            update_group(session, args.id, args.name)
        case ("remove", "Group"):
            remove_group(session, args.id)

        case ("create", "Student"):
            create_student(session, args.name, args.group_id)
        case ("list", "Student"):
            list_students(session)
        case ("update", "Student"):
            update_student(session, args.id, args.name)
        case ("remove", "Student"):
            remove_student(session, args.id)

        case ("create", "Subject"):
            create_subject(session, args.name, args.teacher_id)
        case ("list", "Subject"):
            list_subjects(session)
        case ("update", "Subject"):
            update_subject(session, args.id, args.name)
        case ("remove", "Subject"):
            remove_subject(session, args.id)

        case ("create", "Grade"):
            create_grade(session, args.value, args.student_id, args.subject_id)
        case ("list", "Grade"):
            list_grades(session)

        case _:
            print("Unsupported action or model")

    session.close()


if __name__ == "__main__":
    main()