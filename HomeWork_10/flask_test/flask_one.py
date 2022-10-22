from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, ValidationError
from threading import Lock
import json
from flask.json import jsonify
import os


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
#        validators.Email()
    ])
    job = StringField(label='JOB', validators=[
        validators.Length(min=1, max=35),
        validators.Optional()
    ])


def confirm_password(form, field):
    if form.data['password'] != form.data['confirm_password']:
        raise ValidationError('password not confirm')


class UserForm(FlaskForm):
    email = StringField(label='E-mail', validators=[
        validators.Length(min=5, max=35)#, validators.Email()
    ])
    password = StringField(label='password:', validators =[
        validators.Length(min=6, max=12)
    ])
    confirm_password = StringField(label='confirm password:', validators=[
        validators.Length(min=6, max=20), confirm_password
    ])



app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200


"""
1. По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']
2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму
3. По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'
4. По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля. Необходимо валидировать email, что обязательно присутствует, валидировать
 пароли, что они минимум 6 символов в длину и совпадают. Возрващать пользователю json вида: 
 "status" - 0 или 1 (если ошибка валидации),
 "errors" - список ошибок, если они есть,
 или пустой список.
5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files. Файлы можно туда положить любые текстовые. А если такого нет - 404.
"""

@app.route('/locales')
def locales():
	loc = {
		'ru': 'russian',
		'en': 'english',
		'it': 'international' 
	}
	return json.dumps(loc)


@app.route('/sum/<int:first>/<int:second>')
def user_sum(first, second):
	suma = int(first) + int(second)
	return str(suma)


@app.route('/greet/<user_name>')
def greet(user_name):
	return 'Hello, ' + user_name


@app.route('/form/user', methods=['GET', 'POST'])
def forms():
    if request.method == 'POST':
        user_form = UserForm(request.form)
        status_output = {0:'Проверка пройдена', 1: 'Ошибка валидации'}
        if user_form.validate():
            status_check = jsonify(status_output[0])
            return status_check
        else:
            status_check = jsonify(status_output[1])
            error_list = jsonify(user_form.errors)
            return status_check and error_list
    return 'Done!'


@app.route('/serve/<path:filename>', methods =['GET', 'POST'])
def show_file(filename):
    if not os.path.exists('./files/' + filename):
        return '404: File doesnt exist'
    else:
        opened_file = open('./files/' + filename, 'r')
        read_file = opened_file.read()
        opened_file.close()
    return read_file


if __name__ == '__main__':
    app.run()
