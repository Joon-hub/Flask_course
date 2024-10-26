from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to my Flask app!</h1>"

# Creating a dynamic url using path parameter
@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Welcome {name.title()} to my Flask app!</h1>"

if __name__ == '__main__':
    app.run(debug=True)