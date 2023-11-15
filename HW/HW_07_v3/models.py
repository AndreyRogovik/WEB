from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

# URI: postgresql://username:password@domain:port/database

user = 'postgres'
password = '123456'
domain = 'localhost'
port = '5432'
db = 'postgres'

URI = f"postgresql://{user}:{password}@{domain}:{port}/{db}"

engine = create_engine(URI, echo=True, pool_size=5, max_overflow=0)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    students = relationship('Student', back_populates='group')

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(250), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(250), nullable=False)
    subjects = relationship('Subject', back_populates='teacher')

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teacher', back_populates='subjects')
    grades = relationship('Grade', back_populates='subject')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    grade_date = Column(Date, default=datetime.date.today)
    student = relationship('Student', back_populates='grades')
    subject = relationship('Subject', back_populates='grades')

Base.metadata.create_all(engine)

# Приклад використання:
# group_1 = Group(name='Group A')
# student_1 = Student(fullname='John Doe', group=group_1)
# teacher_1 = Teacher(fullname='Dr. Smith')
# subject_1 = Subject(name='Math', teacher=teacher_1)
# grade_1 = Grade(student=student_1, subject=subject_1, grade=90)

# session.add_all([group_1, student_1, teacher_1, subject_1, grade_1])
# session.commit()
