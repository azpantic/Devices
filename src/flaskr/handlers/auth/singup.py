from flaskr.app import app
from flask import redirect, request, flash, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from ...data_base.models import User , UserTypes
from ...data_base.FDataBase import dBase
from ...loginmanager.UserLogin import UserLogin

@app.route("/signup", methods=["POST", "GET"])
def signup():

    if request.method == "POST":

        form = request.form

        if form["Password"] != form["ConfirmPassword"]:
            flash("Пароли не совпадают")
            return redirect(url_for("signup"))

        if dBase.getUserByEmail(form["Email"]) != None:
            flash("Этот email уже зарегистрирован")
            return redirect(url_for("signup"))

        is_admin = form.get("Admin" , default="") == "on"
        
        user = User(name=form["Name"], email=form["Email"],
                    password=generate_password_hash(form["Password"]),
                    type = UserTypes.administrator if is_admin else UserTypes.regular_user)

        dBase.addUser(user)
        
        login_user(UserLogin().create(user))
        
        return render_template("index.html")

    return render_template("auth/signup.html")
