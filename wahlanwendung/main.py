from flask import render_template, request, session
from wahlanwendung import app, db
from wahlanwendung.models import fragenkat, antwortkat, progrSpr

#for i in db.session.query(fragenkat).order_by(fragenkat.fragennr):
 #  print(i.fragennr, i.frage)

@app.route('/')
def welcome():
    return render_template('startseite.html')

@app.route('/fragenkatalog', methods=["POST","GET"])
def fragenkatalog():
    data = {'fragennr': 1, 'frage': 'Ist es deine erste Programmiersprache, welche du lernen möchtest?'}
    return render_template('fragenkatalog.html', data=data)
""" if request.method == "POST":
        antwort = request.form["answer"]
       if antwort == "a01_01":
           print("ich bin A1")
       elif antwort == "a01_02":
        print("ich bin A2")
       elif antwort == "a01_03":
           print("ich bin A3")
       else:
          print("ich bin A4")
  else:
        return render_template("auswertung.html") """


@app.route('/auswertung')
def auswertung():
    return render_template('auswertung.html')
