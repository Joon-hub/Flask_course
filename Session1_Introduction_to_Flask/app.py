from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to my Flask app!</h1>"

# Example of a path parameter
@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Welcome {name.title()} to my Flask app!</h1>"


# Example of a integer path parameter
@app.route('/add/<int:num1>/<int:num2>')
def addition(num1, num2):
    return (f'{num1} + {num2} = {num1 + num2}')


if __name__ == '__main__':
    app.run(debug=True)

    