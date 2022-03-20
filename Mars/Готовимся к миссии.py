import json

from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<string:title>')
def index(title='Готовимся к миссии'):
    param = {}
    param['title'] = title
    return render_template('base.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


