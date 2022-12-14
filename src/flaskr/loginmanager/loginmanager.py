from flaskr.app import app
from flask_login import LoginManager , current_user
from .UserLogin import UserLogin
from ..data_base.FDataBase import dBase 
from functools import wraps
from flask import abort

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return UserLogin().load_from_DB(user_id , dBase)

def administrator_required(func):
    @wraps(func)
    def decorated_function(*args, **kws):

            if not current_user.is_administrator():
                abort(404)
                
            return func(*args, **kws)  
                  
    return decorated_function