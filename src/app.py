import sqlite3
from fastapi_offline import FastAPIOffline

app = FastAPIOffline()

dbname = 'MoviesInfo.db'

def create_table():
    query = '''
        CREATE TABLE IF NOT EXISTS movies
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        country TEXT,
        year TEXT,
        imdb_rate REAL
        )
                '''
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
#----------------------------------------
create_table()

@app.post("/insert/{title}/{country}/{year}/{imdb_rate}")
def insert_record(title: str, country: str, year: int, imdb_rate: float):
    query =    '''
                INSERT INTO movies(title, country, year, imdb_rate)
                VALUES(?, ?, ?, ?)
               '''
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(query, (title, country, year, imdb_rate))
    conn.commit()
    conn.close()
#----------------------------------------
@app.get("/select_all/")
def select_all_records():
    query = 'SELECT * FROM movies'
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    rows = cursor.execute(query).fetchall()
    conn.close()
    return rows
#----------------------------------------
@app.get("/select_by_id/{id}")
def select_record_by_id(id: int):
    query = 'SELECT * FROM movies WHERE id = ?'
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    rows = cursor.execute(query, (id,)).fetchone()
    conn.close()
    return rows
#----------------------------------------
@app.get("/select_by_name/{title}")
def select_record_by_name(title: str):
    query = 'SELECT * FROM movies WHERE title = ?'
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    rows = cursor.execute(query, (title,)).fetchone()
    conn.close()
    return rows
#----------------------------------------
@app.delete("/delete_by_id/{id}")
def delete_record_by_id(id: int):
    query = '''
DELETE FROM movies WHERE id = ?
'''
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()
    return "Done!"
#----------------------------------------
@app.put("/update_by_id/{id}/{new_imdb_rate}/{new_year}")
def update_record_by_id(id: int, new_imdb_rate: float, new_year: int):
    query = '''
UPDATE movies SET imdb_rate = ? , year = ? WHERE id = ?
'''
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(query, (new_imdb_rate, new_year, id))
    conn.commit()
    conn.close()
    return "Done!"
#python -m uvicorn src.app:app