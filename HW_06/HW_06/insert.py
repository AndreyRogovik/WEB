from faker import Faker
import random
import sqlite3

# Ініціалізуємо генератор випадкових даних
fake = Faker('uk-Ua')

STUDENT_NUMBER = 50
TEACHER_NUMBER = 8
groups = ['Group A', 'Group B', 'Group C']
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']
MIN_SCORE = 60
MAX_SCORE = 100

# Підключення до бази даних
conn = sqlite3.connect('HW.db')
cursor = conn.cursor()

# Заповнюємо таблицю груп
for group in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group,))
    conn.commit()

# Заповнюємо таблицю викладачів
for _ in range(TEACHER_NUMBER): 
    teacher_name = fake.name()
    cursor.execute("INSERT INTO teachers (fullname) VALUES (?)", (teacher_name,))
    conn.commit()

# Заповнюємо таблицю студентів
for _ in range(STUDENT_NUMBER): 
    student_name = fake.name()
    group_id = random.randint(1, len(groups))
    cursor.execute("INSERT INTO students (fullname, group_id) VALUES (?, ?)", (student_name, group_id))
    conn.commit()

# Заповнюємо таблицю предметів
for subject in subjects:
    teacher_id = random.randint(1, TEACHER_NUMBER)  #Bикладач для предмета випадковим чином
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))
    conn.commit()

# Заповнюємо таблицю оцінок
for student_id in range(1, STUDENT_NUMBER):
    for subject_id in range(1, len(subject)+1):
        grade = random.randint(MIN_SCORE, MAX_SCORE)  # Випадкова оцінка
        grade_date = fake.date_of_birth(minimum_age=0, maximum_age=1) #Таким чином форму дату отримання оцінки
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)",
                    (student_id, subject_id, grade, grade_date))
        conn.commit()

# Закриваємо підключення
conn.close()
