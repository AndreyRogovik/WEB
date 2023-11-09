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

    # Встановіть параметр overlaps для відношення student_relationship
    student_relationship = relationship(Student, overlaps="grades,student")


    # Опціонально ви можете встановити каскадне видалення для оцінок, пов'язаних із студентами
    # student = relationship(Student, backref='grades', cascade='all, delete-orphan')

   

Base.metadata.create_all(engine)
Base.metadata.bind = engine

# new_group = Group(name = "X-111")
# session.add(new_group)
# session.commit()


# new_student = Student(fullname= "Alina Morenec", group = new_group)
# session.add(new_student)
# session.commit()

# # Створення та збереження вчителя
# new_teacher = Teacher(fullname="Loza Lozivna")
# session.add(new_teacher)
# session.commit()

# # Створення предмету та прив'язка його до вчителя
# new_subject = Subject(name="XLIB tisto", teacher=new_teacher)
# session.add(new_subject)
# session.commit()


# new_grades = Grade(student_id = new_student.id, subject_id = new_subject.id, grade = 100)
# session.add(new_grades)
# session.commit()

# Створення та збереження студента, групи та вчителя
new_group = Group(name="10 клас")
session.add(new_group)
session.commit()

new_student = Student(fullname="вася", group=new_group)
session.add(new_student)
session.commit()

new_teacher = Teacher(fullname="Снєжна")
session.add(new_teacher)
session.commit()

# Створення та збереження предмету
new_subject = Subject(name="історія", teacher=new_teacher)
session.add(new_subject)
session.commit()

# Отримання ідентифікаторів студента та предмету
student_id = new_student.id
subject_id = new_subject.id

# Створення та збереження оцінки з використанням ідентифікаторів студента та предмету
new_grade = Grade(student_id=student_id, subject_id=subject_id, grade=99)
session.add(new_grade)
session.commit()



# for student in session.query(Student).all():
#     print(student.fullname)