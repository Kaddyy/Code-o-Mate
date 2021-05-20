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
    dataFrage = {'fragennr': 2, 'frage': 'Hier steht eine Frage'}
    dataAntwort = {'antwort1': 'ja', 'antwort2': 'nein'}
    return render_template('fragenkatalog.html', dataFrage=dataFrage, dataAntwort=dataAntwort)

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
