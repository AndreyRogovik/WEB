import sqlite3


# Підключення до бази даних
conn = sqlite3.connect('HW.db')
cursor = conn.cursor()

# Виконати SQL-запит для знаходження середнього балу
cursor.execute("SELECT AVG(grade) FROM grades")
average_grade = cursor.fetchone()[0]

# Закрити підключення до бази даних
conn.close()

# Вивести результат
print()
print("Завдання 4: Знайти середній бал на потоці (по всій таблиці оцінок).")
print(f"Середній бал на потоці: {average_grade}")
