from flask import request, redirect, render_template, url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import Required
from app import app


class Form(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def login():
	# if request.method == 'POST':
 #        form = SignupForm(request.form)
 #        if form.validate():
 #            pass
 #        else:
 #            return render_template('login.html', form = form, page_title = 'Signup to Bio Application')
 #    return render_template('login.html', form = SignupForm(), page_title = 'Signup to Bio Application')
	if 'id' in session:
		return redirect("/main/index")



	return render_template('login.html' )


