import sqlite3


# Підключення до бази даних
conn = sqlite3.connect('HW.db')
cursor = conn.cursor()

# Параметри запиту
subject_name = 'History' 

# Запит для знаходження середнього балу у групах з певного предмета
cursor.execute("""
    SELECT groups.name AS group_name, AVG(grades.grade) AS avg_grade
    FROM students
    INNER JOIN groups ON students.group_id = groups.id
    INNER JOIN grades ON students.id = grades.student_id
    INNER JOIN subjects ON grades.subject_id = subjects.id
    WHERE subjects.name = ?
    GROUP BY groups.id
""", (subject_name,))

# Отримуємо результат запиту
results = cursor.fetchall()

# Виводимо результат у консоль
print(" ")
print("Завдання 3: Знайти середній бал у групах з певного предмета.")
if results:
    print(f"Середній бал у групах за предметом '{subject_name}':")
    for group_name, avg_grade in results:
        print(f"Група: {group_name}, Середній бал: {avg_grade:.2f}")
else:
    print(f"Немає результатів для предмету '{subject_name}'.")

# Закриваємо підключення
conn.close()
