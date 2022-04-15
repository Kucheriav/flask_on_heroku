from flask import Flask, redirect, request, render_template
import os

app = Flask(__name__)
students_dict = {}
students_grades_list = []

def upload_students(parallel=None):
    with open('students.txt', encoding='utf8') as file:
        students = file.read().split('\n')
    for student in students:
        grade, surn, name, login, passw = student.split()
        name = ' '.join(map(lambda x: x.replace("ё", 'е'), [surn, name]))
        if parallel and not grade.startswith(parallel):
            continue
        students_dict[f'{grade}{name}'] = {'login': login, 'passw': passw}
        if grade not in students_grades_list:
            students_grades_list.append(grade)
    students_grades_list.sort()


@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def index():
    if request.method == 'GET':
        return render_template('index.html', title='Распределение',
                               students_grades_list=students_grades_list, error=False, guess=False)
    elif request.method == 'POST':
        user_name = request.form['surname'].strip().replace('ё', 'е')
        print(user_name)
        #форма возвращает номер выбора с единички. user_grade с буквой
        user_grade = students_grades_list[int(request.form['grade']) - 1]
        print(user_name, user_grade)
        if students_dict.get(f'{user_grade}{user_name}'):
            return redirect(f'info/{user_grade}/{user_name}')
        else:
            return render_template('index.html', students_grades_list=students_grades_list, error=True, guess=False,
                                   title='Распределение')

@app.route('/info/<grade>/<name>')
def info(grade, name):
    return render_template('info.html', title='Данные учетки', login=students_dict[f'{grade}{name}']['login'],
                           passw=students_dict[f'{grade}{name}']['passw'])

@app.route('/task/<grade>/<variant>')
def task(grade, variant):
    return render_template('tasks.html', grade=grade[:-1], variant=variant)


# for local tests
# if __name__ == '__main__':
#     upload_students()
#     app.run(port=8080, host='127.0.0.1')


# for heroku
if __name__ == '__main__':
    upload_students()
    port = int(os.environ.get("PORT", 5000))
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')
    app.run(host='0.0.0.0', port=port)
