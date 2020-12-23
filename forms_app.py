from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,
                    BooleanField,
                    DateTimeField,
                    RadioField,
                    SelectField,
                    TextField,
                    TextAreaField,
                    SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY']='mykey'

class TestForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    superuser =  BooleanField("Are you a superuser?")
    location = RadioField('Please choose your location', 
                            choices=[('RGB','Regensburg'),('WAW', 'Warsaw'),('GRZ','Graz')])
    position = SelectField('Your position',
                            choices = [ ('Junior','Junior Engineer'),
                                        ('Developer','Developer'),
                                        ('Senior','Senior Engineer'),
                                        ('Expert','Expert Engineer')])
    notes = TextAreaField()
    submit = SubmitField()


@app.route('/',methods=['GET','POST'])
def index():
    form = TestForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['superuser'] = form.superuser.data
        session['location'] = form.location.data
        session['position'] = form.position.data
        session['notes'] = form.notes.data
        return redirect(url_for('ready'))
    return render_template('index.htm',form=form)

@app.rout('/ready')
def ready():
    return render_template('ready.html')

if __name__ == '__main__':
    app.run(debug = True, 
            host='0.0.0.0')
            
