from flask import Blueprint, render_template, request as req
from model.model import Model

m = Model()
soal = Blueprint("soal", __name__, static_folder="../static", template_folder="../templates")

@soal.route("/dashboard")
def dashboard():
    return render_template("user/dashboard.html")

@soal.route("/soal/<bab>", methods=['GET','POST'])
def bab(bab):
    if req.method == "GET":
        dbsoal = m.generateSoal(bab)
        return render_template("user/bab.html", data={'db': dbsoal, 'endpoint': bab})

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
        return render_template('user/review.html', data={'nilai': int(nilai), 'review':review })
