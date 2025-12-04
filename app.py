from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configura la connessione a PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a@localhost/vini'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disabilita il tracking delle modifiche per ottimizzare le performance

db = SQLAlchemy(app)

# Modello per la tabella
class Vini(db.Model): #usiamo db.model che e un moddelo di poste
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipologia = db.Column(db.String(100), nullable=False)
    regione = db.Column(db.String(100))
    scorta = db.Column(db.Integer)
    costo_unitario = db.Column(db.Numeric(10, 2))
    costo_totale = db.Column(db.Numeric(10, 2))

    def __repr__(self):
        return f'<Vino {self.nome}>'
    
# Home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vini/list')
def listVini():
    vini = Vini.query.all() # Lista completa vini
    return render_template('vini/list.html', vini = vini)

if __name__ == '__main__':
    app.run(debug=True)