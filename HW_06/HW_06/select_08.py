import sqlite3

import sqlite3

# Параметри для пошуку: ім'я викладача
teacher_name = "пані Еріка Арсенич" 

# Підключення до бази даних
conn = sqlite3.connect('HW.db')
cursor = conn.cursor()

# Виконати SQL-запит для знаходження середнього балу викладача зі своїх предметів
cursor.execute("""
    SELECT teachers.fullname, AVG(grades.grade) AS average_grade
    FROM teachers
    JOIN subjects ON teachers.id = subjects.teacher_id
    JOIN grades ON subjects.id = grades.subject_id
    WHERE teachers.fullname = ?
    GROUP BY teachers.fullname
""", (teacher_name,))

average_grade = cursor.fetchone()

# Закрити підключення до бази даних
conn.close()

print()
print("Завдання 8: Знайти середній бал, який ставить певний викладач зі своїх предметів.")
# Вивести результат
if average_grade:
    print(f"Середній бал, який ставить викладач {teacher_name} зі своїх предметів: {average_grade[1]:.2f}")
else:
    print(f"Викладач {teacher_name} не знайдений або не має предметів.")
