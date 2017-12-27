from flask import Flask,session,redirect
from functools import wraps
from flask import request, Response

from modulos.ayudantes import module as ayudantes
from modulos.cursos import module as cursos
from modulos.usuarios import module as usuarios
from modulos.comentarios import module as comentarios
from modulos.main import module as main
from modulos.secciones import module as secciones

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


from models import db,models

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'id' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated


app.db = db
app.models = models
ayudantes.db = db
ayudantes.models = models
cursos.db = db
cursos.models = models
comentarios.db = db
comentarios.models = models
usuarios.db = db
usuarios.models = models
main.db = db
main.models = models
secciones.db = db
secciones.models = models
main.session = session
main.requires_auth = requires_auth




app.config['SECRET_KEY'] = "123456"

app.register_blueprint(ayudantes, url_prefix='/ayudantes')

app.register_blueprint(cursos, url_prefix='/cursos')

app.register_blueprint(usuarios, url_prefix='/usuarios')

app.register_blueprint(comentarios, url_prefix='/comentarios')

app.register_blueprint(main, url_prefix='/main')

app.register_blueprint(secciones, url_prefix='/secciones')


from app import views
