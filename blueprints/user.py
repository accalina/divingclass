from flask import Blueprint, render_template, session
from model.model import Model
user = Blueprint("user", __name__, static_folder="../static", template_folder="../templates")

m = Model()

@user.route('/subscribe')
def subscribe():
    userdata = m.subscription( session['userid'] )
    return render_template('user/subscription.html', data={'userdata':userdata})
    

@user.route('/materi')
def materi():
    books = m.getModule(session['userid'])
    return render_template('user/materi.html', data={'books':books})

@user.route('/soal')
def soallist():
    soal = m.getModule(session['userid'])

    for i, soalname in enumerate(soal):
        soal[i]['name'] = soalname['name'].replace('Modul','Soal')

    return render_template('user/soal.html', data={'soal': soal})
