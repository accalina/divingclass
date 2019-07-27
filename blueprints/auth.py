from flask import Blueprint, render_template, request, session, redirect
from model.model import Model

auth = Blueprint("auth", __name__, static_folder="../static", template_folder="../templates")
m = Model()

# ENDPOINT --------------------------------------+
@auth.route("/")
@auth.route("/index")
def index():
    if 'username' in session:
        return redirect("/dashboard")
    else:
        return redirect("/login?msg=you must Login to continue")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if 'username' not in session:
        if request.method == "GET":
            msg = request.args.get("msg", "")
            return render_template("auth/login.html", data={'msg': msg})

        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            result = m.login(username, password)
            if result != False:
                session['userid'] = result[0]['userid']
                session['username'] = (result[0]['username']).capitalize()
                session['fullname'] = result[0]['fullname']
                session['level'] = result[0]['level']
                return redirect("/dashboard")
            else:
                return redirect(f"/login?msg=Invalid Username / Password")
    else:
        return redirect("/dashboard")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        redirect("/login")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        fullname = request.form.get("fullname")

        m.register(username, password, fullname)
        return redirect(f"/login?msg=user {username} has been created")


@auth.route("/logout")
def logout():
    session.clear()
    return render_template("auth/login.html", data={'msg': 'you have logged out'})
