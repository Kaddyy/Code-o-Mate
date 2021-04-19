from flask import Flask, render_template

app = Flask(__name__)

#das ist unsere erste Seite
@app.route('/')
def welcome():
    return render_template('startseite.html')

if __name__ == '__main__':
    app.run()