from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from my_select import *

DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres"

def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine)

    # Replace these IDs with valid ones from your DB if needed
    subject_id = 1
    teacher_id = 1
    group_id = 1
    student_id = 1

    print("Топ-5 студентів із найвищим середнім балом")
    print(select_1(session))

    print("Студент із найвищим середнім балом з певного предмета")
    print(select_2(session, subject_id))

    print("Середній бал у групах з певного предмета")
    print(select_3(session, subject_id))

    print("Середній бал на потоці (всі оцінки)")
    print(select_4(session))

    print("Які курси читає певний викладач")
    print(select_5(session, teacher_id))

    print("Список студентів у певній групі")
    print(select_6(session, group_id))

    print("Оцінки студентів у групі з певного предмета")
    print(select_7(session, group_id, subject_id))

    print("Середній бал, який ставить певний викладач зі своїх предметів")
    print(select_8(session, teacher_id))

    print("Курси, які відвідує певний студент")
    print(select_9(session, student_id))

    print("Курси, які певному студенту читає певний викладач")
    print(select_10(session, student_id, teacher_id))

    session.close()

if __name__ == "__main__":
    main()
