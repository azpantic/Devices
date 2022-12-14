from flaskr.app import app
from flask import redirect
from flask_login import logout_user , login_required

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
