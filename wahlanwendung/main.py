from flask import render_template, request, session, redirect, url_for
from wahlanwendung import app, db
from wahlanwendung.models import fragenkat, antwortkat, progrSpr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, null

counterJava=0
counterPython = 0
counterSwift = 0
counterCplusplus = 0
counterCsharp = 0
counterJavascript = 0
counterMatlab = 0
counterGo = 0
counterHTMLCSS = 0
counterSQL = 0
counterPHP = 0
counterR = 0
counterTypescript = 0
counterKotlin = 0
counterABAP = 0

@app.route('/')
def welcome():
    return render_template('startseite.html')

@app.route('/fragenkatalog/<int:fragennr>', methods=["POST","GET"])
def fragenkatalog(fragennr):

   #if counterJava != null:
    #   counterJava = 0

    fragennummer = fragennr
    if request.method== 'GET':
        #ABBRUCH: if fragennr = 22 dann hide weiter
        fraage = db.session.query(fragenkat.frage).filter_by(pk_frage_id=fragennummer).scalar()
        dataFrage = {'fragennr': 2, 'frage': fraage}
        antwort1 = db.session.query(fragenkat.antwort1).filter_by(pk_frage_id=fragennummer).scalar()
        antwort2 = db.session.query(fragenkat.antwort2).filter_by(pk_frage_id=fragennummer).scalar()
        antwort3 = db.session.query(fragenkat.antwort3).filter_by(pk_frage_id=fragennummer).scalar()
        #if antwort3 is None:
         #   antwort3 = 'Ulla'
        antwort4 = db.session.query(fragenkat.antwort4).filter_by(pk_frage_id=fragennummer).scalar()
        # if antwort 3 is null hide sö button
        dataAntwort = {'antwort1': antwort1, 'antwort2': antwort2, 'antwort3': antwort3, 'antwort4': antwort4}
        return render_template('fragenkatalog.html', dataFrage=dataFrage, dataAntwort=dataAntwort)
    else:
        answer = request.form.get('answer')
        # if fragennr = 1 oder 2 oder 8 and antwort = nein dann fragennr +=1
        # if fragennr = wirtschaft und antwort nein dann fragennr += 2
        if answer == 'a01_02':
            nachfolger = db.session.query(fragenkat.nachfolger).filter_by(pk_frage_id=fragennummer).scalar()
            if (nachfolger != 0):
                fragennr += nachfolger
        if fragennr < db.session.query(fragenkat).count():
            global counterJava
            counterJava += db.session.query(antwortkat.java).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterPython
            counterPython += db.session.query(antwortkat.python).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterSwift
            counterSwift += db.session.query(antwortkat.swift).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterCplusplus
            counterCplusplus += db.session.query(antwortkat.cplusplus).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterCsharp
            counterCsharp += db.session.query(antwortkat.csharp).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterJavascript
            counterJavascript += db.session.query(antwortkat.javascript).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterMatlab
            counterMatlab += db.session.query(antwortkat.matlab).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterGo
            counterGo += db.session.query(antwortkat.go).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterHTMLCSS
            counterHTMLCSS += db.session.query(antwortkat.htmlcss).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterSQL
            counterSQL += db.session.query(antwortkat.sql).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterPHP
            counterPHP += db.session.query(antwortkat.php).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterR
            counterR += db.session.query(antwortkat.r).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterTypescript
            counterTypescript += db.session.query(antwortkat.typescript).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterKotlin
            counterKotlin += db.session.query(antwortkat.kotlin).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            global counterABAP
            counterABAP += db.session.query(antwortkat.abap).filter_by(fragennummer=fragennr, antwort=answer).scalar()
            print('Java: ', counterJava)
            print('Python: ', counterPython)
            print('Matlab: ', counterMatlab)
            return redirect(url_for('fragenkatalog', fragennr=fragennr + 1))
        else:
            # schreib counter in DB progr_spr
            return render_template('auswertung.html')


@app.route('/auswertung')
def auswertung():
    return render_template('auswertung.html')
