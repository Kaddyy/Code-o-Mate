from flask import render_template, request, session, redirect, url_for
from wahlanwendung import app, db
from wahlanwendung.models import fragenkat, antwortkat, progrSpr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, null


#for i in db.session.query(fragenkat).order_by(fragenkat.fragennr):
 #  print(i.fragennr, i.frage)


@app.route('/')
def welcome():
    return render_template('startseite.html')

@app.route('/fragenkatalog/<int:fragennr>', methods=["POST","GET"])
def fragenkatalog(fragennr):
    if request.method== 'GET':
        fragennummer = fragennr
        #ABBRUCH: if fragennr = 22 dann hide weiter
        fraage = db.session.query(fragenkat.frage).filter_by(pk_frage_id=fragennummer).scalar()
        dataFrage = {'fragennr': 2, 'frage': fraage}
        antwort1 = db.session.query(fragenkat.antwort1).filter_by(pk_frage_id=fragennummer).scalar()
        antwort2 = db.session.query(fragenkat.antwort2).filter_by(pk_frage_id=fragennummer).scalar()
        antwort3 = db.session.query(fragenkat.antwort3).filter_by(pk_frage_id=fragennummer).scalar()
        if antwort3 is None:
            antwort3 = 'Ulla'
        antwort4 = db.session.query(fragenkat.antwort4).filter_by(pk_frage_id=fragennummer).scalar()
        # if antwort 3 is null hide sö button
        dataAntwort = {'antwort1': antwort1, 'antwort2': antwort2, 'antwort3': antwort3, 'antwort4': antwort4}
        return render_template('fragenkatalog.html', dataFrage=dataFrage, dataAntwort=dataAntwort)
    else:
        antwort = request.form.get('answer')
        # hier if-Abfrage und in DB einspeisen
        # if fragennr = 1 oder 2 oder 8 and antwort = nein dann fragennr +=1
        # if fragennr = wirtschaft und antwort nein dann fragennr += 2
        return redirect(url_for('fragenkatalog', fragennr=fragennr + 1))


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
