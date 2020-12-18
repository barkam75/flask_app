from flask import Flask
from flask import render_template
app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')

@app.route('/other')
def other():
    return render_template('test.html')
    

if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0')

