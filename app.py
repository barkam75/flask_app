from flask import Flask
from flask import render_template
app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/other/<name>')
def other(name):
    return render_template('test.html', name = name)
    

if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0')

