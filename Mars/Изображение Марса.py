from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def run():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def advertising():
    text = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!']
    return '</br>'.join(text)


@app.route('/image_mars')
def image():
    return render_template('Изображение Марса.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
