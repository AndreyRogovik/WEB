import sqlite3

# Параметри для пошуку: ім'я студента
student_name = "Оксенія Карась"

# Підключення до бази даних
conn = sqlite3.connect('HW.db')
cursor = conn.cursor()

# Виконати SQL-запит для знаходження курсів, які відвідує студент
cursor.execute("""
    SELECT students.fullname, groups.name, subjects.name
    FROM students
    JOIN groups ON students.group_id = groups.id
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE students.fullname = ?
""", (student_name,))

courses_attended = cursor.fetchall()

# Закрити підключення до бази даних
conn.close()

print()
print("Завдання 9: Знайти список курсів, які відвідує студент.")
# Вивести результат
if courses_attended:
    print(f"Курси, які відвідує студент {student_name}:")
    for row in courses_attended:
        print(f"Група: {row[1]}, Предмет: {row[2]}")
else:
    print(f"Студент {student_name} не знайдений або не відвідує жодних курсів.")
