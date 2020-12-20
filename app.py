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
    error_messages = []
    username = request.args.get('username')
    first = request.args.get('first')
    last = request.args.get('last')
    if not username[-1].isdigit():
        error_messages.append("Username does not have a number as a last character")
    if not any(map(str.isupper, username)):
        error_messages.append("Username does not contain any uppercase characters")
    if not any(map(str.islower, username)):
        error_messages.append("Username does not contain any lowercase characters")
    return render_template('report.html', error_msg = len(error_messages)>0, error_messages=error_messages)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0')

