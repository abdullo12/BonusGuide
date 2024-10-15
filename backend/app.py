import sqlite3
from flask import Flask, request, render_template
import os

app = Flask(__name__, static_folder='static', template_folder='../frontend')

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('backend/scholarships.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def match_scholarships():
    course = request.form['course']
    gpa = float(request.form['gpa'])

    # Подключаемся к базе данных
    conn = get_db_connection()
    scholarships = conn.execute('SELECT * FROM scholarships WHERE course = ? OR course = "4 и выше"', (course,)).fetchall()
    conn.close()
    # Checking all available scholarships in the database
    conn = get_db_connection()
    all_scholarships = conn.execute('SELECT * FROM scholarships').fetchall()
    scholarships_list = [dict(scholarship) for scholarship in all_scholarships]  # Преобразование в словарь
    print(f"Все стипендии: {scholarships_list}")
    conn.close()


    matched_scholarships = {
        "eligible": [],
        "potential": []
    }

    # Сравниваем данные студента с условиями стипендий
    for scholarship in scholarships:
        if gpa >= scholarship['gpa']:
            matched_scholarships["eligible"].append(scholarship['name'])
        else:
            matched_scholarships["potential"].append(scholarship['name'])

    return render_template('results.html', scholarships=matched_scholarships)

if __name__ == '__main__':
    app.run(debug=True)
