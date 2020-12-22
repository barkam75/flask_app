from flask import Flask
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app =  Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

class UserForm(FlaskForm):
    username = StringField('User name')
    submit = SubmitField('Submit')
    

@app.route('/', methods = ['GET','POST'])
def index():
    username = False
    my_form = UserForm()
    if my_form.validate_on_submit():
        username = my_form.username.data
        my_form.username.data = ''
    return render_template('home.html',form=my_form, username=username)

@app.route('/boot')
def boot():
    return render_template('bootstrap_learn.html') 

@app.route('/signup')
def signup():
    return render_template("signup.html")
@app.route('/csslearn')
def csslearn():
    return render_template('csslearn.html')
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0')

#Page refresh command for a page
#<meta http-equiv="refresh" content="30">
