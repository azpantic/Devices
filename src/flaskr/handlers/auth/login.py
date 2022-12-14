from flaskr import data_base
from flaskr.app import app
from flask import redirect , request , flash , url_for , render_template
from werkzeug.security import generate_password_hash , check_password_hash
from ...data_base.models import User 
from ...data_base.FDataBase import dBase
from ...loginmanager.UserLogin import UserLogin
from flask_login import login_user , login_required

from flask_login import current_user

@app.route("/login"  , methods = ["POST" , "GET"])
def login():
    
    if request.method == "GET":

        return render_template("auth/login.html")
    
    if request.method == "POST":
        
        form = request.form
        user = dBase.getUserByEmail(form["Email"])
        
        if user == None:
            flash("Пользователя с таким email не существует") 
            return redirect(url_for("login"))
        
        if not check_password_hash( user.password , form["Password"]):           
            flash("Неверное имя пользователя или пароль") 
            return redirect(url_for("login"))
        
        login_user(UserLogin().create(user))
        
        return redirect("/")
