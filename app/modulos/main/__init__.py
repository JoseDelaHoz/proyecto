from flask import Blueprint, render_template, abort, request,redirect
from jinja2 import TemplateNotFound

from app.login import requires_auth


module = Blueprint('main', __name__,
                        template_folder='templates')


@module.route('/index',methods=["GET","POST"])
@requires_auth
def index():


	return render_template("main_index.html")


@module.route('/login',methods=["POST"])
def login():
	usuario = module.models['usuarios'].query.filter_by(email=request.form["email"]).first()
	if usuario != None and  str(usuario.contrasena) == str(request.form["password"]):
		module.session['id'] = usuario.id
		return redirect("/main/index", code=302)
	else:
		return redirect("/", code=302)
		

@module.route('/logout',methods=["GET"])
def logout():
	del module.session["id"]
	return redirect("/", code=302)

