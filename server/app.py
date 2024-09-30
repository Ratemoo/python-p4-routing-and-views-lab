#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the string in the console
    return parameter  # Display it in the web browser

@app.route('/count/<int:num>')
def count(num):
    # Return a string with numbers from 0 to num - 1, separated by newlines
    return '\n'.join(str(i) for i in range(num)) + '\n'  # Add a newline at the end to match expected output

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    
    return str(result)  # Return the result as a string

if __name__ == '__main__':
    app.run(debug=True)
