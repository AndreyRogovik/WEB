import sqlite3

# Параметр, що представляє назву групи, для якої ви хочете знайти студентів
group_name = "Group A"  

# Підключення до бази даних
conn = sqlite3.connect('HW.db')
cursor = conn.cursor()

# Виконати SQL-запит для знаходження студентів у групі
cursor.execute("""
    SELECT students.fullname
    FROM students
    JOIN groups ON students.group_id = groups.id
    WHERE groups.name = ?
""", (group_name,))

students_in_group = cursor.fetchall()

# Закрити підключення до бази даних
conn.close()

print()
print("Завдання 6: Знайти список студентів у певній групі.")
# Вивести результат
print(f"Список студентів у групі {group_name}:")
for student in students_in_group:
    print(student[0])
