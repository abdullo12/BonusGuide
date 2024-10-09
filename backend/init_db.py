import sqlite3

# Подключаемся к базе данных (если файла еще нет, он будет создан)
conn = sqlite3.connect('scholarships.db')
c = conn.cursor()

# Создаем таблицу для стипендий
c.execute('''
CREATE TABLE IF NOT EXISTS scholarships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    gpa REAL NOT NULL,
    amount REAL NOT NULL
)
''')

# Вставляем данные о стипендиях
c.execute('''
INSERT INTO scholarships (name, course, gpa, amount)
VALUES ('Стипендия Генерального директора для аспирантов', 'аспирантура', 4.0, 11500)
''')

c.execute('''
INSERT INTO scholarships (name, course, gpa, amount)
VALUES ('Стипендия Генерального директора для 4-го курса и выше', '4 и выше', 4.0, 7000)
''')

# Сохраняем изменения и закрываем подключение
conn.commit()
conn.close()
