# -*- coding: utf-8 -*-
from flask import render_template
from flask_login import login_required
from ext import app, socketio
from apps.auth import auth
from apps.contact import contact
from apps.todo import todo
from apps.tools import tool
from apps.service import svm
from apps.notifications import ntfy
from apps.message import msg
from apis.user import authapi
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(contact, url_prefix='/contact')
app.register_blueprint(todo, url_prefix='/todo')
app.register_blueprint(tool, url_prefix='/tool')
app.register_blueprint(svm, url_prefix='/svm')
app.register_blueprint(ntfy, url_prefix='/ntfy')
app.register_blueprint(authapi, url_prefix='/api')
app.register_blueprint(msg, url_prefix='/msg')


@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
@login_required
def index():
    return render_template("index.html")


if __name__ == '__main__':
    socketio.run(app, debug=True, use_reloader=False)
