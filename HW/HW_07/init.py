import random
from faker import Faker
from sqlalchemy.exc import SQLAlchemyError
from db import session
from models import Group, Student, Teacher, Grade, Subject

fake = Faker('uk-UA')

STUDENT_NUMBER = 50
TEACHER_NUMBER = 8
MIN_SCORE = 60
MAX_SCORE = 100
GROUPS = ['Group 1', 'Group 2', 'Group 3']
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']


#Заповнюємо таблицю груп
def insert_groups():
    for item in GROUPS:
        group = Group(name=item)
        session.add(group)
    


# Заповнюємо таблицю викладачів
def insert_teachers():
    for _ in range(TEACHER_NUMBER): 
        teacher = Teacher(fullname = fake.name())
        session.add(teacher)
        session.commit()

# Заповнюємо таблицю студентів
def insert_students():
    for _ in range(STUDENT_NUMBER): 
        student = Student(fullname = fake.name(), group_id = random.randint(1, len(GROUPS)))
        session.add(student)
    session.commit()   

# Заповнюємо таблицю предметів
def insert_subjects():   
    for item in subjects:
        subject = Subject(name = item, teacher_id = random.randint(1, TEACHER_NUMBER))
        session.add(subject)
    session.commit()
def insert_grades():
    for st_id in range(1, STUDENT_NUMBER + 1):
        for subj_id in range(1, len(subjects) + 1):
            grade = Grade(
                student_id = st_id,
                subject_id = subj_id,
                grade = random.randint(MIN_SCORE, MAX_SCORE),
                grade_date = fake.date_of_birth(minimum_age=0, maximum_age=1)
            )
            session.add(grade)
    session.commit()

if __name__ == '__main__':
    try:
        insert_groups()
        insert_teachers()
        insert_students()
        insert_subjects()
        insert_grades()
 
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()

