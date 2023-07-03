#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def user(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route("/count/<int:parameter>")
def count(parameter):
    count = ''
    for num in range(parameter):
        count += (f'{num}\n')
    return count
    #probably wants it printed instead like the top one
    #

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    # number = (num1) (operation) (num2)
    # return number
    number = 1.0
    if operation == '+':
        number = num1 + num2
    elif operation == '-':
        number = num1 - num2
    elif operation == '*':
        number = num1 * num2
    elif operation == '/':
        number = num1 // num2
    elif operation == '%':
        number = num1 % num2
    return str(number)

if __name__ == '__main__':
    app.run(port=5555, debug=True)