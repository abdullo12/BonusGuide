from flask import Flask, request, render_template
import sqlite3
import os

# Указываем правильный путь к папке с шаблонами
app = Flask(__name__, static_folder='static', template_folder='../frontend')

# Получаем абсолютный путь к базе данных
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'scholarships.db')

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Обработка формы
@app.route('/submit', methods=['POST'])
def match_scholarships():
    # Получаем данные из формы
    course = int(request.form['course'])
    gpa = float(request.form['gpa'])
    education_form = request.form['education_form']
    citizenship = request.form['citizenship']
    research = request.form['research']
    social_activity = request.form['social_activity']
    sports_activity = request.form['sports_activity']
    social_status = request.form['social_status']
    internship = request.form['internship']

    # Подключаемся к базе данных
    conn = get_db_connection()
    cursor = conn.cursor()

    # Запрос для поиска подходящих стипендий
    query = '''
    SELECT * FROM scholarships 
    WHERE (course LIKE ? OR course = "Любая")
    AND gpa <= ? 
    AND (education_form = ? OR education_form = "Любая")
    AND (citizenship = ? OR citizenship = "Любая")
    AND (research = ? OR research = "Любая")
    AND (social_activity = ? OR social_activity = "Любая")
    AND (sports_activity = ? OR sports_activity = "Любая")
    AND (social_status = ? OR social_status = "Любая")
    AND (internship = ? OR internship = "Любая")
    '''
    cursor.execute(query, (f'%{course}%', gpa, education_form, citizenship, research, social_activity, sports_activity, social_status, internship))
    scholarships = cursor.fetchall()
    conn.close()

    # Разделяем стипендии на подходящие и потенциальные
    matched_scholarships = {
        "eligible": [],
        "potential": []
    }

    for scholarship in scholarships:
        if (scholarship['gpa'] <= gpa and
            (scholarship['education_form'] == education_form or scholarship['education_form'] == 'Любая') and
            (scholarship['citizenship'] == citizenship or scholarship['citizenship'] == 'Любая') and
            (scholarship['research'] == research or scholarship['research'] == 'Любая') and
            (scholarship['social_activity'] == social_activity or scholarship['social_activity'] == 'Любая') and
            (scholarship['sports_activity'] == sports_activity or scholarship['sports_activity'] == 'Любая') and
            (scholarship['social_status'] == social_status or scholarship['social_status'] == 'Любая') and
            (scholarship['internship'] == internship or scholarship['internship'] == 'Любая')):
            matched_scholarships["eligible"].append(scholarship)
        else:
            matched_scholarships["potential"].append(scholarship)

    return render_template('results.html', scholarships=matched_scholarships)

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)