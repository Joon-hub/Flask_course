import time 
from flask import Flask , redirect, url_for 

# initialize the app 
app = Flask(__name__)

# create a route to the homepage
@app.route('/')
def home():
    return "<h1> Welcome to Joon App </h1>"

@app.route('/passed')
def passed():
    return "<h1> Congrats you have succesfully completed the course</h1>"


@app.route('/failed')
def failed():
    return "<h1> Sorry, you have failed the course. Please re-register for the course </h1>"

@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num > 60:
        # redirect user to passed page
        return redirect(url_for('passed'))
    else:
        # redirect user to failed page
        return redirect(url_for('failed'))

        
# return the main function
if __name__ == '__main__':
    app.run(debug=True)
