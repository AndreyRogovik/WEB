import random 
from models import session, Group, Student, Subject, Teacher, Grade
from sqlalchemy.exc import SQLAlchemyError
from faker import Faker


fake = Faker('uk-UA')

STUDENT_NUMBER = 50
TEACHER_NUMBER = 8
MIN_SCORE = 60
MAX_SCORE = 100
GROUPS = ['GroupA', 'GroupB', 'GroupC']
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']

#Заповнюємо таблицю груп
def insert_groups():
    for item in GROUPS:
        group = Group(name = item)
        session.add(group)
    
# Заповнюємо таблицю викладачів
def insert_teachers():
    for _ in range(TEACHER_NUMBER): 
        teacher = Teacher(fullname = fake.name())
        session.add(teacher)
        

# Заповнюємо таблицю студентів
def insert_students():
    for _ in range(STUDENT_NUMBER): 
        student = Student(fullname = fake.name(), group_id = random.randint(1, len(GROUPS)))
        session.add(student)
     

# Заповнюємо таблицю предметів
def insert_subjects():   
    for item in subjects:
        subject = Subject(name = item, teacher_id = random.randint(1, TEACHER_NUMBER))
        session.add(subject)
    
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


if __name__ == '__main__':
    try:
        insert_groups()
        insert_teachers()
        insert_students()
        insert_subjects()
        insert_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()