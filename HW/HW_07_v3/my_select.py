from sqlalchemy import func
from models import session, Student, Grade, Subject, Group, Teacher

def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    result = (
        session.query(
            Student.fullname,
            func.avg(Grade.grade).label('avg_grade')
        )
        .join(Grade, Student.id == Grade.student_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
        .all()
    )
    print('5 студентів із найбільшим середнім балом з усіх предметів')
    for row in result:
        print(row.fullname, round(row.avg_grade, 2))


def select_2(subject_name):
    # Знайти студента із найвищим середнім балом з певного предмета
    result = (
        session.query(
            Student.fullname,
            func.avg(Grade.grade).label('avg_grade')
        )
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .first()
    )
    if result:
        print(f"студент із найвищим середнім балом з {subject_name}:")
        print(result.fullname, round(result.avg_grade, 2))
    else:
        print(f"На жаль, немає даних для предмета {subject_name}")


def select_3(subject_name):
    result = (
        session.query(Group.name, func.avg(Grade.grade).label('avg_grade'))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Group.id)
        .order_by(func.avg(Grade.grade).desc())
        .all()
    )

    if result:
        print(f"Середній бал з предмета {subject_name} у групах:")
        for group_name, avg_grade in result:
            print(f"{group_name}: {avg_grade:.2f}")
    else:
        print(f"На жаль, немає даних для предмета {subject_name}")
        
def select_4(subject_name):
    # Знайти середній бал на потоці (по всій таблиці оцінок)
    result = (
        session.query(func.avg(Grade.grade).label('avg_grade'))
        .scalar()
    )
    if result:
        print(f"Середній бал на потоці: з предмету {subject_name} - {round(result, 2)}")
    else:
        print(f'Нажаль оцынок для визначення середнього балу недостатньо')

def select_5(teacher_name):
    # Знайти які курси читає певний викладач
    result = (
        session.query(Subject.name)
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .filter(Teacher.fullname == teacher_name)
        .all()
    )
    if result:
        print(f"Викладач {teacher_name} читає наступні курси:")
        for row in result:
            print(row.name)
    else:
        print(f"Викладача {teacher_name} не знайдено.")

def select_6(group_name):
    # Знайти список студентів у певній групі
    result = (
        session.query(Student.fullname)
        .join(Group, Student.group_id == Group.id)
        .filter(Group.name == group_name)
        .all()
    )
    if result:
        print(f"Студенти групи {group_name}:")
        for row in result:
            print(row.fullname)
    else:
        print(f"Групи {group_name} не знайдено.")
        

def select_7(group_name, subject_name):
    # Знайти оцінки студентів у окремій групі з певного предмета
    result = session.query(
        Student.fullname,
        Grade.grade
    ).join(Grade).join(Subject).join(Group).filter(Group.name == group_name, Subject.name == subject_name).all()
    
    print(f'Оцінки студентів у групі {group_name} з предмета - {subject_name}:')
    
    if result:
        for row in result:
            print(row.fullname, row.grade)
    else:
        print("Немає оцінок для цієї групи та предмета.")
        
        
def select_8(teacher_name):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів
    result = session.query(
        Teacher.fullname,
        Subject.name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Subject, Teacher.subjects).join(Grade).filter(Teacher.fullname == teacher_name).group_by(Teacher.fullname, Subject.name).all()
    
    print(f'Середній бал, який ставить викладач {teacher_name} зі своїх предметів:')
    
    if result:
        for row in result:
            print(f'{row.fullname}, {row.name}: {round(row.avg_grade, 2)}')
    else:
        print("Результат визначити не вдалось")

def select_9(student_name):
    # Знайти список курсів, які відвідує певний студент
    result = session.query(
        Subject.name
    ).join(Grade).join(Student).filter(Student.fullname == student_name).distinct().all()
    if result:
        print(f"Курси, які відвідує студент {student_name}:")
        for row in result:
            print(row.name)
    else:
        print('Студент не відвідує курсів, він ледар')


def select_10(student_name, teacher_name):
    # Список курсів, які певному студенту читає певний викладач
    result = session.query(
        Subject.name
    ).join(Grade).join(Student).join(Teacher).filter(Student.fullname == student_name, Teacher.fullname == teacher_name).distinct().all()

  
    if result:
        print(f"Курси які читає викладач {teacher_name} для студента {student_name}:")
        for row in result:
            print(row.name)
    else:
        print(f"викладач {teacher_name} не читає курсів для студента {student_name}:")


        

