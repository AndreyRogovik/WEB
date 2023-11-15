# Знайти які курси читає певний викладач.
import sqlite3


# Параметр, що представляє ім'я викладача, для якого ви хочете знайти курси
teacher_name = "Софія Дрозд"

# Підключення до бази даних
conn = sqlite3.connect('HW.db')
cursor = conn.cursor()

# Виконати SQL-запит для знаходження курсів викладача
cursor.execute("""
    SELECT subjects.name
    FROM subjects
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE teachers.fullname = ?
""", (teacher_name,))

courses_taught = cursor.fetchall()

# Закрити підключення до бази даних
conn.close()

# Вивести результат
print()
print("Завдання 5: Знайти які курси читає певний викладач.")
print(f"Викладач {teacher_name} читає наступні курси:")
for course in courses_taught:
    print(course[0])
