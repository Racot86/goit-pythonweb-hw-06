# seed.py
from faker import Faker
import random
from datetime import date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from models import Group, Student, Teacher, Subject, Grade

fake = Faker()

engine = create_engine("postgresql://postgres:password@localhost:5432/postgres", echo=False)
session = Session(bind=engine)

# Створення груп
groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

# Створення викладачів
teachers = [Teacher(name=fake.name()) for _ in range(4)]
session.add_all(teachers)
session.commit()

# Створення предметів
subjects = [
    Subject(name=fake.word().capitalize(), teacher=random.choice(teachers))
    for _ in range(6)
]
session.add_all(subjects)
session.commit()

# Створення студентів
students = [
    Student(name=fake.name(), group=random.choice(groups))
    for _ in range(45)
]
session.add_all(students)
session.commit()

# Створення оцінок
for student in students:
    for subject in subjects:
        for _ in range(random.randint(10, 20)):
            grade = Grade(
                value=round(random.uniform(60, 100), 2),
                date=fake.date_between(start_date='-6m', end_date='today'),
                student=student,
                subject=subject
            )
            session.add(grade)

session.commit()
session.close()

print("✅ Seed data inserted successfully.")