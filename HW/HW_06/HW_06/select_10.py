import sqlite3

# Параметри для пошуку: ім'я студента та ім'я викладача
student_name = "Сніжана Гавриш" 
teacher_name = "Орина Єресько"  

# Підключення до бази даних
conn = sqlite3.connect('HW.db')
cursor = conn.cursor()

# Виконати SQL-запит для знаходження курсів, які відвідує студент у викладача
cursor.execute("""
    SELECT students.fullname, groups.name, subjects.name
    FROM students
    JOIN groups ON students.group_id = groups.id
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE students.fullname = ? AND teachers.fullname = ?
""", (student_name, teacher_name))

courses_attended = cursor.fetchall()

# Закрити підключення до бази даних
conn.close()

print()
print("Завдання 10: Список курсів, які певному студенту читає певний викладач.")
# Вивести результат
if courses_attended:
    print(f"Курси, які відвідує студент {student_name} у викладача {teacher_name}:")
    for row in courses_attended:
        print(f"Група: {row[1]}, Предмет: {row[2]}")
else:
    print(f"Студент {student_name} не відвідує курси викладача {teacher_name} або такий студент або викладач не знайдений.")
