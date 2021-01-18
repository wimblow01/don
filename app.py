# import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import pymongo
from pprint import pprint
from connexion import Connexion
# from mdp import mdp, user



app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

@app.route('/')
def index():
    donate = Connexion.compteur()
    return render_template('index.html', donate = donate)

@app.route('/conditions')
def conditions():
    return render_template('conditions.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/donateurs')
def donateurs():
    leo = Connexion.leonardo()
    brad = Connexion.brad()
    donator = Connexion.donator()
    return render_template('donateurs.html', leo=leo, brad=brad, donator=donator)



@app.route('/formulaire', methods=('GET', 'POST'))
def formulaire():
    if request.method == 'POST':
        don = request.form['don']
        name = request.form['name']
        fname = request.form['fname']
        adresse = request.form['adresse']
        mail = request.form['mail']

        if not don:
            flash('Veuillez renseigner un don!')
        elif not name:
            flash('Veuillez renseigner un nom')
        elif not fname:
            flash('Veuillez renseigner un prénom')
        elif not adresse:
            flash('Veuillez renseigner un adresse')
        elif not mail:
            flash('Veuillez renseigner un mail')
        else:
            Connexion.open_db()
            Connexion.don.insert_one({"name":name, "fname":fname, "adresse":adresse, "mail":mail, "don":int(don)} )
            Connexion.close_db()
            return redirect(url_for('index'))

    return render_template('formulaire.html')

if __name__ == '__main__':
    app.run(port=5000)