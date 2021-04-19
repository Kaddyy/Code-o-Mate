from flask import Flask

app = Flask(__name__)

#das ist unsere erste Seite
@app.route('/')
def welcome():
    return "Willkommen!"




if __name__ == '__main__':
    app.run()