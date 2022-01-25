from ast import FloorDiv
from flask import Flask, render_template, request    

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def rootpage():
    name =""
    food=""
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        food = request.form.get('userfood')
    return render_template("index.html", name = name, food = food)


"""@app.route("/potato")
def welcome1():
    return 'There is a potato in my app'

@app.route("/bob")
def welcome2():
    return 'Hey Bob!'

@app.route('/method', methods = ['GET', 'POST'])
def method():
    if request.method == 'POST':
        return "This is a POST request"
    else:
        return "Probably getting GET request"
"""

app.run()