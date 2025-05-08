from flask import Blueprint, render_template, request, flash
from calculator_app.calculator import Calculator

main_bp = Blueprint('main', __name__)
calculator = Calculator()

@main_bp.route('/', methods=['GET'])
def index():
    return render_template('calculator/index.html', result=None)

@main_bp.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form.get('num1', '')
    num2 = request.form.get('num2', '')
    operation = request.form.get('operation', '')
    
    result = None
    error_message = None
    
    try:
        num1 = float(num1)
        num2 = float(num2)
        
        if operation == 'add':
            result = calculator.add(num1, num2)
        elif operation == 'subtract':
            result = calculator.subtract(num1, num2)
        elif operation == 'multiply':
            result = calculator.multiply(num1, num2)
        elif operation == 'divide':
            result = calculator.divide(num1, num2)
        else:
            error_message = "Invalid operation"
            
    except ValueError as e:
        if "divide by zero" in str(e).lower():
            error_message = "Cannot divide by zero"
        else:
            error_message = "Invalid input"
    
    return render_template('calculator/index.html', 
                           result=result, 
                           error_message=error_message,
                           num1=num1 if isinstance(num1, (int, float)) else '',
                           num2=num2 if isinstance(num2, (int, float)) else '',
                           operation=operation)