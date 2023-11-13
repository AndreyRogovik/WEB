from sqlalchemy import Column, Integer, String, ForeignKey,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
