from flask import Flask, redirect, request, url_for, render_template
import os
app = Flask(__name__)
#возможны проблемы с 10 11. точно будут с про.группами
#пока берем с веб-морды название класса целиком и передаем :-1
#в определитель вариантов и def task
VARIANTS_DICT = {
    '7': 2,
    '9': 3
}
students_dict = {}
students_grades_list = []

def upload_students(parallel=None):
    with open('students.txt', encoding='utf8') as file:
        students = file.read().split('\n')
    for student in students:
        grade, name = student.split('\t')
        name = name.replace('ё', 'е')
        if parallel and not grade.startswith(parallel):
            continue
        if grade not in students_dict:
            students_dict[grade] = [name]
            students_grades_list.append(grade)
        else:
            students_dict[grade].append(name)
    students_grades_list.sort()


@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def index():
    if request.method == 'GET':
        return render_template('index.html', students_grades_list=students_grades_list, error=False, guess=False)
    elif request.method == 'POST':
        user_name = request.form['surname'].strip().replace('ё', 'е')
        print(user_name)
        #форма возвращает номер выбора с единички. user_grade с буквой
        user_grade = students_grades_list[int(request.form['grade']) - 1]
        print(user_name, user_grade)
        if user_name in students_dict[user_grade]:
            #по ключу берем список. в нем по элементу - номер. модулируем кол-вом варинатов для этой паралелли без буквы
            variant = students_dict[user_grade].index(user_name) % VARIANTS_DICT[user_grade[:-1]] + 1
            return redirect(f'task/{user_grade}/{variant}')
        else:
            print(students_dict[user_grade])
            user_name = user_name.strip().lower().split()
            for student_name in students_dict[user_grade]:
                if user_name[0] in student_name.lower():
                    return render_template('index.html', students_grades_list=students_grades_list,
                                           error=True, guess=student_name)
            if len(user_name) == 2:
                for student_name in students_dict[user_grade]:
                    if user_name[1] in student_name.lower():
                        return render_template('index.html', students_grades_list=students_grades_list,
                                               error=True, guess=student_name)
            return render_template('index.html', students_grades_list=students_grades_list, error=True, guess=False)

@app.route('/task/<grade>/<variant>')
def task(grade, variant):
    return render_template('tasks.html', grade=grade[:-1], variant=variant)


# for local tests
# if __name__ == '__main__':
#     upload_students()
#     app.run(port=8080, host='127.0.0.1')
#
# for heroku
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')
    app.run(host='0.0.0.0', port=port)
