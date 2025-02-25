import sqlite3

def init_db():
    conn = sqlite3.connect(r'C:\Users\Abdullo\Desktop\-\backend\scholarships.db')
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scholarships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        course TEXT NOT NULL,
        gpa REAL NOT NULL,
        education_form TEXT,
        citizenship TEXT,
        research TEXT,
        social_activity TEXT,
        sports_activity TEXT,
        social_status TEXT,
        internship TEXT
    )
    ''')

    # Вставка тестовых данных
    cursor.executemany('''
    INSERT INTO scholarships (name, course, gpa, education_form, citizenship, research, social_activity, sports_activity, social_status, internship)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', [
        ('Государственная академическая стипендия', '1-5 курс', 4.0, 'Очная', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет'),
        ('Повышенная государственная академическая стипендия', '2-5 курс', 5.0, 'Очная', 'Нет', 'Любая', 'Любая', 'Любая', 'Нет', 'Да'),
        ('Стипендия Генерального директора для аспирантов', '1-5 курс', 4.0, 'Очная', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет', 'Нет'),
        ('Государственная социальная стипендия', '1-5 курс', 0.0, 'Очная', 'Нет', 'Нет', 'Нет', 'Нет', 'Да', 'Нет'),
        ('Государственная академическая и (или) государственная…', '1-2 курс', 4.0, 'Очная', 'Нет', 'Нет', 'Нет', 'Нет', 'Да', 'Нет'),
        ('Именные стипендии ОАО "РЖД"', '3-5 курс', 4.0, 'Очная', 'Нет', 'Да', 'Нет', 'Нет', 'Нет', 'Нет'),
        ('Стипендия имени Иноземцева В.Г.', '3-5 курс', 4.0, 'Очная', 'Нет', 'Да', 'Нет', 'Нет', 'Нет', 'Нет'),
        ('Стипендия имени П.П.Мельникова', '2-5 курс', 4.0, 'Очная', 'Нет', 'Да', 'Нет', 'Нет', 'Нет', 'Нет'),
        ('Стипендия имени С.П.Королева', '2-5 курс', 4.0, 'Очная', 'Нет', 'Да', 'Нет', 'Нет', 'Нет', 'Нет')
    ])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()