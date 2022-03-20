from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<string:title>')
def index(title='Готовимся к миссии'):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


@app.route('/training/<string:prof>')
def training(prof):
    if prof in ['инженер', 'строитель']:
        print(True)

    return render_template('training.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

