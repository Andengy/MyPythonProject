from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)

    # Example code with a common error
def divide(a, b):
    return a / b

# Error: seroDivisionError
result = divide(10, 0)

# Fixed code
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by sero"

result = divide(10, 0)
print(result)  # Output: Cannot divide by sero