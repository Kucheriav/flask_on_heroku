from flask import Flask, redirect, request, url_for
import os


with open('students.txt', encoding='utf8') as file:
    students = file.read().split('\n')
students_dict = {}
students_grades = []
for student in students:
    temp = student.split()
    if temp[0] not in students_dict:
        students_dict[temp[0]] = [temp[1]]
        students_grades.append(temp[0])
    else:
        students_dict[temp[0]].append(temp[1])
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def index():
    if request.method == 'GET':
        return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
                        <style>
                               form {
                                width: 500px; 
                               }
                              </style>
                        <title>Распределение</title>
                      </head>
                      <body>
                        <form method="post">
                            <h1>Выберите класс</h1> 
                            <select name="grade" class="form-select">
                              <option value="1">9а</option>
                              <option value="2">9б</option>
                              <option value="3">9в</option>
                            </select>                  
                            <h1>Введите фамилию</h1>                        
                            <input name="surname">
                            <button type="submit" class="btn btn-primary btn-sm">Отправить</button>
                        </form>
                      </body>
                    </html>'''
    elif request.method == 'POST':
        surname = request.form['surname'].capitalize().strip().replace('ё', 'е')
        print(surname)
        grade = students_grades[int(request.form['grade']) -1]
        print(surname, grade)
        if surname in students_dict[grade]:
            variant = students_dict[grade].index(surname) % 3 + 1
            return redirect(f'result/{variant}')
        else:
            return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
                        <style>
                               form {
                                width: 500px; 
                               }
                              </style>
                        <title>Распределение</title>
                      </head>
                      <body>
                        <form method="post">
                            <h1>Ошибка ввода: проверьте класс и фамилию!</h1>
                            <h1>Выберите класс</h1> 
                            <select name="grade" class="form-select">
                              <option value="1">9а</option>
                              <option value="2">9б</option>
                              <option value="3">9в</option>
                            </select>                  
                            <h1>Введите фамилию</h1>                        
                            <input name="surname">
                            <button type="submit" class="btn btn-primary btn-sm">Отправить</button>
                        </form>
                      </body>
                    </html>'''

@app.route('/result/<variant>')
def result(variant):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Распределение</title>
                      </head>
                      <body>
                        <image src="{url_for('static',filename = f'{variant}.jpg')}" >
                        <img src="/static/{variant}.jpg" alt='Что-то пошло не так'>
                      </body>
                    </html>'''




# for local tests
# if __name__ == '__main__':
#     app.run(port=8080, host='127.0.0.1')

# for heroku
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
