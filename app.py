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

class MapForm(FlaskForm):
    zoom = StringField('Zoom')
    submit = SubmitField('Submit')
    

@app.route('/', methods = ['GET','POST'])
def index():
    username = False
    my_form = UserForm()
    if my_form.validate_on_submit():
        username = my_form.username.data
        my_form.username.data = ''
    return render_template('home.html',form=my_form, username=username)

@app.route('/map', methods = ['GET','POST'])
def leaflet_map():
    zoom =10
    zoom_form = MapForm()
    if zoom_form.validate_on_submit():
        zoom = zoom_form.zoom.data
    return render_template('map.html',form=zoom_form, zoom=zoom)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0')

#Page refresh command for a page
#<meta http-equiv="refresh" content="30">

#Maps leaflet.js, Tilestache, Mapbox Studio
