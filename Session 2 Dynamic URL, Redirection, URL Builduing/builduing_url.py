import time 
from flask import Flask , redirect, url_for 

# initialize the app 
app = Flask(__name__)

# create a route to the homepage
@app.route('/')
def home():
    return "<h1> Welcome to Joon App </h1>"

@app.route('/passed/<sname>/<int:marks>')
def passed(sname, marks):
    return f"<h1> Congrats {sname.title()} have succesfully completed the course with {marks} marks</h1>"


@app.route('/failed/<sname>/<int:marks>')
def failed(sname, marks):
    return f"<h1> Sorry, {sname.title()} have failed the course with {marks} marks and the passing marks are 60. Please re-register for the course </h1>"

@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num > 60:
        # redirect user to passed page
        return redirect(url_for('passed',sname=name, marks=num))
    else:
        # redirect user to failed page
        return redirect(url_for('failed',sname=name, marks=num))

        
# return the main function
if __name__ == '__main__':
    app.run(debug=True)