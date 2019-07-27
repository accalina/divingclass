from flask import Blueprint, render_template, session, redirect, request as req
from model.model import Model
user = Blueprint("user", __name__, static_folder="../static", template_folder="../templates")

m = Model()

# HELPER ----------------------------------------+
def is_loggedin():
    if 'username' in session:
        return True       

# ENDPOINT --------------------------------------+

@user.route("/dashboard")
def dashboard():
    if is_loggedin():
        sidebar = {'parent': 'dashboard', 'child': 'dashboard'}
        return render_template("user/dashboard.html", data={'sidebar':sidebar})
    else:
        return redirect("/login")

@user.route('/subscribe')
def subscribe():
    if is_loggedin():
        sidebar = {'parent': 'dashboard', 'child': 'subscribe'}
        userdata = m.subscription( session['userid'] )
        return render_template('user/subscription.html', data={'userdata':userdata, 'sidebar': sidebar})
    else:
        return redirect("/login")
    

@user.route('/materi')
def materi():
    if is_loggedin():
        sidebar = {'parent': 'materi', 'child': 'materi'}
        books = m.getModule(session['userid'])
        return render_template('user/materi.html', data={'books': books, 'sidebar': sidebar})
    else:
        return redirect("/login")

@user.route('/soal')
def soallist():
    if is_loggedin():
        sidebar = {'parent': 'materi', 'child': 'soal'}
        soal = m.getModule(session['userid'])
        for i, soalname in enumerate(soal):
            soal[i]['name'] = soalname['name'].replace('Modul','Soal')

        return render_template('user/soal.html', data={'soal': soal, 'sidebar': sidebar})
    else:
        return redirect("/login")


@user.route("/soal/<bab>", methods=['GET','POST'])
def bab(bab):
    if is_loggedin():
        sidebar = {'parent': 'materi', 'child': 'soal'}
        if req.method == "GET":
            dbsoal = m.generateSoal(bab)
            return render_template("user/bab.html", data={'db': dbsoal, 'endpoint': bab, 'sidebar': sidebar})

        if req.method == "POST":
            soal = {
                '1': req.form.get('soal1'),
                '2': req.form.get('soal2'),
                '3': req.form.get('soal3'),
                '4': req.form.get('soal4'),
                '5': req.form.get('soal5'),
                '6': req.form.get('soal6'),
                '7': req.form.get('soal7'),
                '8': req.form.get('soal8'),
                '9': req.form.get('soal9'),
                '10': req.form.get('soal10'),
            }

            jawab = {
                '1': req.form.get('jawab1'),
                '2': req.form.get('jawab2'),
                '3': req.form.get('jawab3'),
                '4': req.form.get('jawab4'),
                '5': req.form.get('jawab5'),
                '6': req.form.get('jawab6'),
                '7': req.form.get('jawab7'),
                '8': req.form.get('jawab8'),
                '9': req.form.get('jawab9'),
                '10': req.form.get('jawab10'),
            }

            nilai, review = m.comparing(soal, jawab)
            return render_template('user/review.html', data={'nilai': int(nilai), 'review': review, 'sidebar': sidebar})
    else:
        return redirect("/login")
