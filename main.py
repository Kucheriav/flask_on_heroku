from flask import Flask, redirect, request
import os
seven_a_list = ['Авдеев Илья',
'Алексеева Евгения',
'Алферова Варвара',
'Басулина Евангелина',
'Безверхний Артём',
'Богоявленская Анна',
'Бычков Герман',
'Волняков Александр',
'Демидов Иван',
'Ермилова Елена',
'Иванов Андрей',
'Карпунина Ульяна',
'Карташова Дарья',
'Касьянова Арина',
'Кирюхина Мария',
'Комлева Анастасия',
'Королев Михаил',
'Кузнецова Ксения',
'Кунька Екатерина',
'Лаврушина Ангелина',
'Мозгин Тихон',
'Ненашев Владимир',
'Орешко Валерий',
'Помосова Виктория',
'Рожкова Арина',
'Сучков Артем',
'Сучкова Валерия',
'Терехов Кирилл',
'Федоров Родион',
'Хомич София М.',
'Шолохова Елизавета',
'Шундрина Елизавета',
'Юрцев Кирилл',
'Юрчак Глеб',
'Яковлева Арина А']
seven_a_dict = {}
c = 0
for name in seven_a_list:
    seven_a_dict[name.split()[0]] = c % 2 + 1
    c += 1
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
                        <title>Распределение</title>
                      </head>
                      <body>
                        <h1>Введите фамилию</h1>
                        <form method="post">
                            <input name="code">
                            <button type="submit" class="btn btn-primary btn-sm">Отправить</button>
                        </form>
                      </body>
                    </html>'''
    elif request.method == 'POST':
        data = request.form['code'].capitalize().strip().replace('ё', 'е')
        if data in seven_a_dict:
            return redirect(f'result/{seven_a_dict[data]}')
        else:
            return '''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                                    <title>Распределение</title>
                                  </head>
                                  <body>
                                    <h1>Ошибка ввода: вводите только фамилию и только в именительном падеже</h1>
                                    <form method="post">
                                        <input name="code">
                                        <button type="submit" class="btn btn-primary btn-sm">Отправить</button>
                                    </form>
                                  </body>
                                </html>'''
@app.route('/result/<code>')
def result(code):
    if code == '1':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>Распределение</title>
                          </head>
                          <body>
                            <h1>Ваша ссылка на тест</h1>
                            <a href='https://forms.gle/qmkVmLMKGkcx6d4v7'> начать </a>
                          </body>
                        </html>'''
    elif code == '2':
        return '''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <title>Распределение</title>
                                  </head>
                                  <body>
                                    <h1>Ваша ссылка на тест</h1>
                                    <a href='https://forms.gle/etmZi7nsngPXektL8'> начать </a>
                                  </body>
                                </html>'''
    else:
        return '''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <title>Распределение</title>
                                  </head>
                                  <body>
                                    <h1>Неправильный код!</h1>
                                  </body>
                                </html>'''



# for local tests
# if __name__ == '__main__':
#     app.run(port=8080, host='127.0.0.1')

# for heroku
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)