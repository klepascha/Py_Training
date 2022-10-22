from flask import Flask

app = Flask(__name__)


@app.route('/hello/<user>')
def home(user):
    return 'hello, user: ' + user


@app.route('/summ/<num1><num2>')
def summ(num1, num2):
    summs = int(num1) + int(num2)
    return 'Summ: ' + str(summs)


if __name__ == '__main__':
    app.run()
