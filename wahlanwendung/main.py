from flask import render_template, request
from wahlanwendung import app, db, models

#das ist unsere erste Seite
@app.route('/')
def welcome():
    return render_template('startseite.html')

@app.route('/fragenkatalog', methods=["POST","GET"])
def fragenkatalog():
  #  if request.method == "POST":
   #     antwort = request.form["answer"]
     #   if antwort == "a01_01":
      #      print("ich bin A1")
      #  elif antwort == "a01_02":
       #     print("ich bin A2")
      #  elif antwort == "a01_03":
        #    print("ich bin A3")
    #    else:
    #        print("ich bin A4")
  #  else:
      #  return render_template("auswertung.html")

    return render_template('fragenkatalog.html')

@app.route('/auswertung')
def auswertung():
    return render_template('auswertung.html')
