# -*- coding: utf-8 -*-
from flask import Blueprint

ntfy = Blueprint('ntfy',
                 __name__,
                 # template_folder='/opt/auras/templates/',   #指定模板路径
                 # static_folder='/opt/auras/flask_bootstrap/static/',#指定静态文件路径
                 )

import views
