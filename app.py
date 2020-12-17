from flask import Flask
from flask import render_template
app =  Flask(__name__)

@app.route('/')
def index():
    name_list = {1,2,3,4,5}
    my_variable='bartek'
    return render_template('basic.html',my_variable=my_variable,list=name_list)

@app.route('/other/<name>')
def other(name):
    if name[-1:] == "y":
        return name[:-1] + "iful"
    else:
        return name + "y"

if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0')

