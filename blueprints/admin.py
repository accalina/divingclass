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
        paymentlist = m.getUnverifiedPayment()
        userlist, adminlist = m.getAdminInfo()
        data = {
            'sidebar': sidebar,
            'userlist': userlist,
            'usercount': len(userlist),
            'adminlist': adminlist,
            'admincount': len(adminlist),
            'paymentlist': paymentlist
        }
        return render_template("admin/dashboard.html", data=data)
    else:
        return redirect("/login")

@admin.route('/verified')
def verified():
    if is_loggedin():
        userid = request.args.get('id','')
        
        result = m.verified(userid)        
        if result:
            return redirect('/admin')
        else:
            return "There's an error on verifying the payment data, please contact administrator"
    else:
        return redirect("/login")
