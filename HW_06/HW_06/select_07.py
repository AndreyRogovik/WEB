import sqlite3

# Параметри для пошуку: назва групи та назва предмета
group_name = "Group A"  
subject_name = "Math" 

# Підключення до бази даних
conn = sqlite3.connect('HW.db')
cursor = conn.cursor()

# Виконати SQL-запит для знаходження оцінок студентів у заданій групі та предметі
cursor.execute("""
    SELECT students.fullname, grades.grade
    FROM students
    JOIN groups ON students.group_id = groups.id
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE groups.name = ? AND subjects.name = ?
""", (group_name, subject_name))

grades_in_group_and_subject = cursor.fetchall()

# Закрити підключення до бази даних
conn.close()

print()
print("Завдання 7: Знайти оцінки студентів у окремій групі з певного предмета.")
# Вивести результат
print(f"Оцінки студентів у групі {group_name} з предмета {subject_name}:")
for student, grade in grades_in_group_and_subject:
    print(f"{student}: {grade}")
