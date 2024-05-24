import sqlite3

def init_db():
    conn = sqlite3.connect('student_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS progress (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    quiz_results TEXT,
                    learning_path INTEGER
                )''')
    conn.commit()
    conn.close()

def save_progress(name, quiz_results, learning_path):
    conn = sqlite3.connect('student_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO progress (name, quiz_results, learning_path) VALUES (?, ?, ?)",
              (name, str(quiz_results), learning_path))
    conn.commit()
    conn.close()

# Initialize the database
init_db()
