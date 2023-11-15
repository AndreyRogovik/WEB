import sqlite3


# Підключення до бази даних
conn = sqlite3.connect('HW.db')
cursor = conn.cursor()

# Запит для знаходження студента із найвищим середнім балом з математики
cursor.execute("""
    SELECT students.id, students.fullname, AVG(grades.grade) AS avg_grade
    FROM students
    INNER JOIN grades ON students.id = grades.student_id
    INNER JOIN subjects ON grades.subject_id = subjects.id
    WHERE subjects.name = 'Math'
    GROUP BY students.id, students.fullname
    ORDER BY avg_grade DESC
    LIMIT 1
""")

# Отримуємо результат запиту
result = cursor.fetchone()

# Виводимо результат у консоль
print(" ")
print("Завдання 2: Знайти студента із найвищим середнім балом з певного (математика) предмета.")

if result:
    student_id, student_name, avg_grade = result
    print(f"Student ID: {student_id}, Name: {student_name}, Average Grade in Math: {avg_grade}")
else:
    print("No students found for Math subject.")

# Закриваємо підключення
conn.close()
