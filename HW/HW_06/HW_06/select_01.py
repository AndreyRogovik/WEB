import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('HW.db')
cursor = conn.cursor()

# Виконуємо запит для знаходження 5 студентів із найвищими середніми балами
cursor.execute("""
    SELECT *
    FROM (
      SELECT
        students.id AS student_id,
        students.fullname AS student_name,
        AVG(grades.grade) AS avg_grade
      FROM students
      LEFT JOIN grades ON students.id = grades.student_id
      GROUP BY students.id, students.fullname
    ) AS avg_grades
    ORDER BY avg_grade DESC
    LIMIT 5
""")

# Отримуємо результат запиту
results = cursor.fetchall()

# Виводимо результати у консоль
print(" ")
print("Завдання 1: Знайти 5 студентів із найбільшим середнім балом з усіх предметів.")

for row in results:
    print(f"Student ID: {row[0]}, Name: {row[1]}, Average Grade: {row[2]}")

# Закриваємо підключення
conn.close()
