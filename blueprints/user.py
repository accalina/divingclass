from flask import Blueprint, render_template, session, redirect, request as req
from model.model import Model
from datetime import datetime as d
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
        userscore = m.getUserScore(session['userid'])
        sidebar = {'parent': 'dashboard', 'child': 'dashboard'}
        return render_template("user/dashboard.html", data={'sidebar': sidebar, 'userscore': userscore})
    else:
        return redirect("/login")

@user.route('/subscribe', methods=["GET","POST"])
def subscribe():
    if is_loggedin():
        if req.method == "GET":
            sidebar = {'parent': 'dashboard', 'child': 'subscribe'}
            userdata = m.subscription( session['userid'] )
            return render_template('user/subscription.html', data={'userdata':userdata, 'sidebar': sidebar})
        if req.method == "POST":
            module = req.form.get("module","")
            uploadfile = req.files['uploadfile']
            extension = (uploadfile.filename).split('.')[-1]
            time = str(d.now()).split('.')[0].split(' ')[1].replace(':', '-')
            filename = "{}_{}_bukti-pembayaran_{}.{}".format( session['userid'], module, time ,extension)
            uploadfile.save("static/uploads/{}".format(filename))
            result = m.buyModule(session['userid'], module, filename)

            if result:
                return redirect('/subscribe')
            else:
                return "Buy Module Failed, Please contact Administrator for more info"

    else:
        return redirect("/login")
    
@user.route('/profile', methods=["GET","POST"])
def profile():
    if is_loggedin():
        if req.method == "GET":
            sidebar = {'parent': 'account', 'child': 'profile'}
            userdata = (session['username']).lower()
            return render_template('user/profile.html', data={'userdata': userdata, 'sidebar': sidebar})

        if req.method == "POST":
            username = req.form.get("username","")
            fullname = req.form.get("fullname","")

            result = m.updateProfile( session['userid'], username, fullname )
            if result:
                session['username'] = (username).capitalize()
                session['fullname'] = fullname
                return redirect('/profile')
            else:
                return "Error Updating Profile!"
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
        if bab != 'final':
            sidebar = {'parent': 'materi', 'child': 'soal'}
        else:
            sidebar = {'parent': 'ujian', 'child': 'uas'}

        if req.method == "GET":

            bablist = ['bab2', 'bab3', 'bab4', 'bab5', 'bab6', 'final']
            if bab in bablist:
                result = m.checkPreviousScore(session['userid'], bab)
                if result:
                    dbsoal = m.generateSoal(bab)
                    return render_template("user/bab.html", data={'db': dbsoal, 'endpoint': bab, 'sidebar': sidebar, 'module':bab})
                else:
                    return "Anda harus menyelesaikan tes sebelumnya dengan nilain minimal 7 terlebih dahulu"
            else:
                dbsoal = m.generateSoal(bab)
                return render_template("user/bab.html", data={'db': dbsoal, 'endpoint': bab, 'sidebar': sidebar, 'module':bab})

        if req.method == "POST":
            module = req.form.get('module')
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
            result = m.saveScore(session['userid'], module, nilai)
            if result:
                return render_template('user/review.html', data={'nilai': int(nilai), 'review': review, 'sidebar': sidebar})
            else:
                return "Saving Score failed, please contact Administrator!"
    else:
        return redirect("/login")
