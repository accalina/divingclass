from flask import Blueprint, render_template, request, session, redirect
from model.model import Model
admin = Blueprint("admin", __name__, static_folder="../static", template_folder="../templates")

m = Model()

# HELPER ----------------------------------------+
def is_loggedin():
    if 'username' in session:
        if session['level'] == 9:
            return True       

# ENDPOINT --------------------------------------+

@admin.route('/admin')
def dashboard():
    if is_loggedin():
        sidebar = {'parent': 'dashboard', 'child': 'dashboard'}
        userlist, adminlist = m.getAdminInfo()
        data = {
            'sidebar': sidebar,
            'userlist': userlist,
            'usercount': len(userlist),
            'adminlist': adminlist,
            'admincount': len(adminlist)

        }
        return render_template("admin/dashboard.html", data=data)
    else:
        return redirect("/login")
