from app import app
from flask import Flask, render_template

@app.route('/index')
@app.route('/test')
@app.route('/test2')
def index():
    #return "hello human ;-;"
    user = {"username": "R"}
    return render_template('test.html', user = user)

@app.route('/rianisadoodoo')
@app.route('/')
@app.route('/home')
def home():
    a = "My name is"
    return """ 
    <html>
        <head>
            <title> Home - Sample Flask App</title>
        </head>
        <body>
            <div><a href="/test">Test Page</a></div>
            <div><a href="/test2">Test2 Page</a></div>
    """ \
    + a + \
    """     </body>
    </html>
    """