from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, мир!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

# for heroku
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)