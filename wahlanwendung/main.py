from flask import render_template, request, session, redirect, url_for
from wahlanwendung import app, db
from wahlanwendung.models import fragenkat, antwortkat, progrSpr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, null, update

SPRACHE_HTML_CSS__SCALAR = db.session.query(progrSpr.helloWorld).filter_by(sprache='HTML/CSS').scalar()

counterJava = 0
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
    fragennummer = fragennr
    if request.method== 'GET':
        #ABBRUCH: if fragennr = 22 dann hide weiter button
        fraage = db.session.query(fragenkat.frage).filter_by(pk_frage_id=fragennummer).scalar()
        dataFrage = {'frage': fraage}
        antwort1 = db.session.query(fragenkat.antwort1).filter_by(pk_frage_id=fragennummer).scalar()
        antwort2 = db.session.query(fragenkat.antwort2).filter_by(pk_frage_id=fragennummer).scalar()
        antwort3 = db.session.query(fragenkat.antwort3).filter_by(pk_frage_id=fragennummer).scalar()
        antwort4 = db.session.query(fragenkat.antwort4).filter_by(pk_frage_id=fragennummer).scalar()
        # if antwort 3 is null hide sö radios
        dataAntwort = {'antwort1': antwort1, 'antwort2': antwort2, 'antwort3': antwort3, 'antwort4': antwort4}
        return render_template('fragenkatalog.html', dataFrage=dataFrage, dataAntwort=dataAntwort)
    else:
        answer = request.form.get('answer')
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
            #print('C++: ', counterCplusplus)
            if answer == 'a01_02':
                nachfolger = db.session.query(fragenkat.nachfolger).filter_by(pk_frage_id=fragennummer).scalar()
                if (nachfolger != 0):
                    fragennr += nachfolger
            return redirect(url_for('fragenkatalog', fragennr=fragennr + 1))
        else:
            return render_template('auswertung.html')


@app.route('/auswertung')
def auswertung():
    # hier Daten in DB
    db.session.query(progrSpr).filter_by(sprache='Java').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterJava}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='Python').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterPython}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='Swift').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterSwift}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='C++').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterCplusplus}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='C#').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterCsharp}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='JavaScript').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterJavascript}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='Matlab').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterMatlab}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='Go').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterGo}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='HTML/CSS').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterHTMLCSS}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='SQL').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterSQL}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='PHP').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterPHP}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='R').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterR}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='TypeScript').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterTypescript}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='Kotlin').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterKotlin}, synchronize_session=False)
    db.session.query(progrSpr).filter_by(sprache='ABAP').update({progrSpr.absolutes_erg: progrSpr.absolutes_erg + counterABAP}, synchronize_session=False)
    db.session.commit()
    individuell = {'Java': counterJava, 'Python':counterPython, 'Swift':counterSwift, 'Cplusplus':counterCplusplus, 'Csharp':counterCsharp, 'JavaScript':counterJavascript, 'Matlab':counterMatlab, 'Go':counterGo, 'HTMLCSS':counterHTMLCSS, 'SQL':counterSQL, 'PHP':counterPHP, 'R':counterR, 'TypeScript':counterTypescript, 'Kotlin':counterKotlin, 'ABAP':counterABAP}
    #gesamt = query alles zusammen zählen
    ges = 0
    sprachenanz = db.session.query(progrSpr).count() + 1
    for i in range(1, sprachenanz):
        erg = db.session.query(progrSpr.absolutes_erg).filter_by(pk_id=i).scalar()
        ges += erg
       ## print('erg:', i, erg)
    #15 mal absolutes_erg / gesamt
    #get gesamter Wert
    gesJava = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='Java').scalar() / ges
    gesPython = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='Python').scalar() / ges
    gesSwift = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='Swift').scalar() / ges
    gesCplusplus = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='C++').scalar() / ges
    gesCsharp = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='C#').scalar() / ges
    gesJavaScript = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='JavaScript').scalar() / ges
    gesMatlab = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='Matlab').scalar() / ges
    gesGo = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='Go').scalar() / ges
    gesHTMLCSS = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='HTML/CSS').scalar() / ges
    gesSQL = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='SQL').scalar() / ges
    gesPHP = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='PHP').scalar() / ges
    gesR = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='R').scalar() / ges
    gesTS = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='TypeScript').scalar() / ges
    gesKotlin = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='Kotlin').scalar() / ges
    gesABAP = db.session.query(progrSpr.absolutes_erg).filter_by(sprache='ABAP').scalar() / ges
    gesamt = {'Java': gesJava, 'Python':gesPython, 'Swift':gesSwift, 'Cplusplus':gesCplusplus, 'Csharp':gesCsharp, 'JavaScript':gesJavaScript, 'Matlab':gesMatlab, 'Go':gesGo, 'HTMLCSS':gesHTMLCSS, 'SQL':gesSQL, 'PHP':gesPHP, 'R':gesR, 'TypeScript':gesTS, 'Kotlin':gesKotlin, 'ABAP':gesABAP}

    #get Beschreibungen
    beschrJava = db.session.query(progrSpr.beschreibung).filter_by(sprache='Java').scalar()
    beschrPython = db.session.query(progrSpr.beschreibung).filter_by(sprache='Python').scalar()
    beschrSwift = db.session.query(progrSpr.beschreibung).filter_by(sprache='Swift').scalar()
    beschrCplusplus = db.session.query(progrSpr.beschreibung).filter_by(sprache='C++').scalar()
    beschrCsharp = db.session.query(progrSpr.beschreibung).filter_by(sprache='C#').scalar()
    beschrJavaScript = db.session.query(progrSpr.beschreibung).filter_by(sprache='JavaScript').scalar()
    beschrMatlab = db.session.query(progrSpr.beschreibung).filter_by(sprache='Matlab').scalar()
    beschrGo = db.session.query(progrSpr.beschreibung).filter_by(sprache='Go').scalar()
    beschrHTMLCSS = db.session.query(progrSpr.beschreibung).filter_by(sprache='HTML/CSS').scalar()
    beschrSQL = db.session.query(progrSpr.beschreibung).filter_by(sprache='SQL').scalar()
    beschrPHP = db.session.query(progrSpr.beschreibung).filter_by(sprache='PHP').scalar()
    beschrR = db.session.query(progrSpr.beschreibung).filter_by(sprache='R').scalar()
    beschrTS = db.session.query(progrSpr.beschreibung).filter_by(sprache='TypeScript').scalar()
    beschrKotlin = db.session.query(progrSpr.beschreibung).filter_by(sprache='Kotlin').scalar()
    beschrABAP = db.session.query(progrSpr.beschreibung).filter_by(sprache='ABAP').scalar()
    beschreibungen = {'Java': beschrJava, 'Python': beschrPython, 'Swift': beschrSwift, 'Cplusplus': beschrCplusplus,
               'Csharp': beschrCsharp, 'JavaScript': beschrJavaScript, 'Matlab': beschrMatlab, 'Go': beschrGo,
               'HTMLCSS': beschrHTMLCSS, 'SQL': beschrSQL, 'PHP': beschrPHP, 'R': beschrR, 'TypeScript': beschrTS,
               'Kotlin': beschrKotlin, 'ABAP': beschrABAP}

    # get erste Links
    linkJava = db.session.query(progrSpr.link1).filter_by(sprache='Java').scalar()
    linkPython = db.session.query(progrSpr.link1).filter_by(sprache='Python').scalar()
    linkSwift = db.session.query(progrSpr.link1).filter_by(sprache='Swift').scalar()
    linkCplusplus = db.session.query(progrSpr.link1).filter_by(sprache='C++').scalar()
    linkCsharp = db.session.query(progrSpr.link1).filter_by(sprache='C#').scalar()
    linkJavaScript = db.session.query(progrSpr.link1).filter_by(sprache='JavaScript').scalar()
    linkMatlab = db.session.query(progrSpr.link1).filter_by(sprache='Matlab').scalar()
    linkGo = db.session.query(progrSpr.link1).filter_by(sprache='Go').scalar()
    linkHTMLCSS = db.session.query(progrSpr.link1).filter_by(sprache='HTML/CSS').scalar()
    linkSQL = db.session.query(progrSpr.link1).filter_by(sprache='SQL').scalar()
    linkPHP = db.session.query(progrSpr.link1).filter_by(sprache='PHP').scalar()
    linkR = db.session.query(progrSpr.link1).filter_by(sprache='R').scalar()
    linkTS = db.session.query(progrSpr.link1).filter_by(sprache='TypeScript').scalar()
    linkKotlin = db.session.query(progrSpr.link1).filter_by(sprache='Kotlin').scalar()
    linkABAP = db.session.query(progrSpr.link1).filter_by(sprache='ABAP').scalar()
    links = {'Java': linkJava, 'Python': linkPython, 'Swift': linkSwift, 'Cplusplus': linkCplusplus,
             'Csharp': linkCsharp, 'JavaScript': linkJavaScript, 'Matlab': linkMatlab, 'Go': linkGo,
             'HTMLCSS': linkHTMLCSS, 'SQL': linkSQL, 'PHP': linkPHP, 'R': linkR, 'TypeScript': linkTS,
             'Kotlin': linkKotlin, 'ABAP': linkABAP}
    # get link2
    link2Java = db.session.query(progrSpr.link2).filter_by(sprache='Java').scalar()
    link2Python = db.session.query(progrSpr.link2).filter_by(sprache='Python').scalar()
    link2Swift = db.session.query(progrSpr.link2).filter_by(sprache='Swift').scalar()
    link2Cplusplus = db.session.query(progrSpr.link2).filter_by(sprache='C++').scalar()
    link2Csharp = db.session.query(progrSpr.link2).filter_by(sprache='C#').scalar()
    link2JavaScript = db.session.query(progrSpr.link2).filter_by(sprache='JavaScript').scalar()
    link2Matlab = db.session.query(progrSpr.link2).filter_by(sprache='Matlab').scalar()
    link2Go = db.session.query(progrSpr.link2).filter_by(sprache='Go').scalar()
    link2HTMLCSS = db.session.query(progrSpr.link2).filter_by(sprache='HTML/CSS').scalar()
    link2SQL = db.session.query(progrSpr.link2).filter_by(sprache='SQL').scalar()
    link2PHP = db.session.query(progrSpr.link2).filter_by(sprache='PHP').scalar()
    link2R = db.session.query(progrSpr.link2).filter_by(sprache='R').scalar()
    link2TS = db.session.query(progrSpr.link2).filter_by(sprache='TypeScript').scalar()
    link2Kotlin = db.session.query(progrSpr.link2).filter_by(sprache='Kotlin').scalar()
    link2ABAP = db.session.query(progrSpr.link2).filter_by(sprache='ABAP').scalar()
    links2 = {'Java': link2Java, 'Python': link2Python, 'Swift': link2Swift, 'Cplusplus': link2Cplusplus,
              'Csharp': link2Csharp, 'JavaScript': link2JavaScript, 'Matlab': link2Matlab, 'Go': link2Go,
              'HTMLCSS': link2HTMLCSS, 'SQL': link2SQL, 'PHP': link2PHP, 'R': link2R, 'TypeScript': link2TS,
              'Kotlin': link2Kotlin, 'ABAP': link2ABAP}
    # get hello Worlds
    hW2Java = db.session.query(progrSpr.helloWorld).filter_by(sprache='Java').scalar()
    hW2Python = db.session.query(progrSpr.helloWorld).filter_by(sprache='Python').scalar()
    hW2Swift = db.session.query(progrSpr.helloWorld).filter_by(sprache='Swift').scalar()
    hW2Cplusplus = db.session.query(progrSpr.helloWorld).filter_by(sprache='C++').scalar()
    hW2Csharp = db.session.query(progrSpr.helloWorld).filter_by(sprache='C#').scalar()
    hW2JavaScript = db.session.query(progrSpr.helloWorld).filter_by(sprache='JavaScript').scalar()
    hW2Matlab = db.session.query(progrSpr.helloWorld).filter_by(sprache='Matlab').scalar()
    hW2Go = db.session.query(progrSpr.helloWorld).filter_by(sprache='Go').scalar()
    hW2HTMLCSS = db.session.query(progrSpr.helloWorld).filter_by(sprache='HTML/CSS').scalar()
    hW2SQL = db.session.query(progrSpr.helloWorld).filter_by(sprache='SQL').scalar()
    hW2PHP = db.session.query(progrSpr.helloWorld).filter_by(sprache='PHP').scalar()
    hW2R = db.session.query(progrSpr.helloWorld).filter_by(sprache='R').scalar()
    hW2TS = db.session.query(progrSpr.helloWorld).filter_by(sprache='TypeScript').scalar()
    hW2Kotlin = db.session.query(progrSpr.helloWorld).filter_by(sprache='Kotlin').scalar()
    hW2ABAP = db.session.query(progrSpr.helloWorld).filter_by(sprache='ABAP').scalar()
    #print(hW2Java)
    print(hW2ABAP)
    p_ = '<p>Hello World</%p>'
    helloWorlds = {'Java': hW2Java, 'Python': hW2Python, 'Swift': hW2Swift, 'Cplusplus': hW2Cplusplus,
                   'Csharp': hW2Csharp, 'JavaScript': hW2JavaScript, 'Matlab': hW2Matlab, 'Go': hW2Go,
                   'HTMLCSS': hW2HTMLCSS, 'SQL': hW2SQL, 'PHP': hW2PHP, 'R': hW2R, 'TypeScript': hW2TS,
                   'Kotlin': hW2Kotlin, 'ABAP': hW2ABAP}
    return render_template('auswertung.html', individuell=individuell, beschreibungen=beschreibungen, gesamt=gesamt, links=links, links2=links2, helloWorlds=helloWorlds)


print("""System.out.println("Hello World");""")
