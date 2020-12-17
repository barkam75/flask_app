from flask import Flask
from flask import render_template
app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/other/<name>')
def other(name):
    if name[-1:] == "y":
        return name[:-1] + "iful"
    else:
        return name + "y"

if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0')

