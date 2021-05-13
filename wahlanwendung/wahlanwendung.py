from flask import render_template
from wahlanwendung import app, db, models

#das ist unsere erste Seite
@app.route('/')
def welcome():
    return render_template('startseite.html')

@app.route('/fragenkatalog')
def fragenkatalog():
    return render_template('fragenkatalog.html')

@app.route('/auswertung')
def auswertung():
    return render_template('auswertung.html')
