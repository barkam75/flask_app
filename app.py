from flask import Flask
from flask import render_template, request
app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/other')
def signup():
    return render_template('signup.html')

@app.route('/thank')
def thank_you():
    username = request.args.get('username')
    first = request.args.get('first')
    last = request.args.get('last')
    if username[-1].isdigit():
        contains_digit = True
    else:
        contains_digit = False

    contains_uppercase = any(map(str.isupper, username))
    contains_lowercase = any(map(str.islower, username))

    return render_template('report.html', contains_digit=contains_digit, contains_uppercase=contains_uppercase, contains_lowercase=contains_lowercase)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0')

