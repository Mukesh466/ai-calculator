from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""
    error = ""

    if request.method == 'POST':
        choice = request.form.get('choice')
        num1 = request.form.get('num1', '')
        num2 = request.form.get('num2', '')

        try:
            if choice == '1':  # Addition
                result = float(num1) + float(num2)

            elif choice == '2':  # Subtraction
                result = float(num1) - float(num2)

            elif choice == '3':  # Multiplication
                result = float(num1) * float(num2)

            elif choice == '4':  # Division
                if float(num2) == 0:
                    error = "Cannot divide by zero"
                else:
                    result = float(num1) / float(num2)

            elif choice == '5':  # Power
                result = float(num1) ** float(num2)

            elif choice == '6':  # Square Root
                if float(num1) < 0:
                    error = "Square root not possible for negative numbers"
                else:
                    result = math.sqrt(float(num1))

            elif choice == '7':  # Factorial
                n = int(float(num1))
                if n < 0:
                    error = "Factorial not possible"
                else:
                    result = math.factorial(n)

            elif choice == '8':  # Modulus
                result = float(num1) % float(num2)

            else:
                error = "Invalid Choice"

        except ValueError:
            error = "Please enter valid numbers"
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)