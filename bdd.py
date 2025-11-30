import sqlite3

def init_db():
    conn = sqlite3.connect('notes.db')  # Ouvre ou crée le fichier notes.db
    cursor = conn.cursor()
    
    # Création de la table 'notes'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Base de données 'notes.db' et table 'notes' initialisées.")