from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'notes.db'

# Fonction utilitaire pour connecter à la BDD
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # Permet d'accéder aux colonnes par nom
    return conn

@app.route('/', methods=('GET', 'POST'))
def index():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes ORDER BY timestamp DESC').fetchall()
    conn.close()
    
    # Si la méthode est POST, l'utilisateur a soumis le formulaire
    if request.method == 'POST':
        # 1. Récupérer le texte soumis
        note_content = request.form['note_content']
        
        if not note_content:
            # Gérer l'erreur si le champ est vide
            return 'Le contenu ne peut pas être vide!', 400
        
        # 2. Stocker dans la BDD
        conn = get_db_connection()
        conn.execute('INSERT INTO notes (content) VALUES (?)', (note_content,))
        conn.commit()
        conn.close()
        
        # Rediriger pour éviter la soumission multiple
        return redirect(url_for('index'))

    # Si la méthode est GET, afficher la page et les notes existantes
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    # Lance l'application en mode développement
    app.run(debug=True)