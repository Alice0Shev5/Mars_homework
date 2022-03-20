from PIL import Image

from flask import Flask, url_for, render_template, request

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


@app.route('/image_sample')
def image_sample():
    return render_template('Изображение Марса.html')


@app.route('/promotion_image')
def promotion_image():
    return render_template('Реклама с картинкой.html')


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('Отбор астронавтов.html')
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        prof = ['prof1', 'prof2', 'prof3', 'prof4', 'prof5', 'prof6', 'prof7', 'prof8']
        for el in prof:
            if request.form.get(el):
                print(el, request.form[el])
        print(request.form['sex'])
        print(request.form['about'])
        f = request.files['file']
        print(f.read())

        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')