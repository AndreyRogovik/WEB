import random
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from faker import Faker

engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres', echo=False)

DBSession = sessionmaker(bind=engine)
session = DBSession()


Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship(Group)
    grades = relationship('Grade', backref='student', cascade='all, delete-orphan')
    
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250), nullable=False)

class Subject(Base):
    __tablename__ = 'subjects'   
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship(Teacher)
    grades = relationship('Grade', backref='subject', cascade='all, delete-orphan')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    grade_date = Column(Date)
    student_relationship = relationship(Student, overlaps="grades,student")

   

Base.metadata.create_all(engine)
Base.metadata.bind = engine



# Ініціалізуємо генератор випадкових даних
fake = Faker('uk-Ua')

STUDENT_NUMBER = 50
TEACHER_NUMBER = 8
MIN_SCORE = 60
MAX_SCORE = 100
groups = ['Group A', 'Group B', 'Group C']
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']

#Заповнюємо таблицю груп
for item in groups:
    group = Group(name=item)
    session.add(group)
session.commit()

# Заповнюємо таблицю викладачів
for _ in range(TEACHER_NUMBER): 
    teacher = Teacher(fullname = fake.name())
    session.add(teacher)
session.commit()    

# Заповнюємо таблицю студентів
for _ in range(STUDENT_NUMBER): 
    student = Student(fullname = fake.name(), group_id = random.randint(1, len(groups)))
    session.add(student)
session.commit()

# Заповнюємо таблицю предметів
for item in subjects:
    subject = Subject(name = item, teacher_id = random.randint(1, TEACHER_NUMBER))
    session.add(subject)
session.commit()

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

