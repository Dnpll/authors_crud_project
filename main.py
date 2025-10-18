from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sqlite3
import os
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

DB_NAME = "/tmp/authors.db"

class Author(BaseModel):
    name: str
    country: str

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country TEXT
    
    )""")
    cur.execute("SELECT COUNT(*) FROM authors")
    if cur.fetchone()[0] == 0:
     cur.executemany("INSERT INTO authors (name, country) VALUES (?, ?)", [
        ("Ernest Hemingway", "United States"),
        ("Jane Austen", "United Kingdom"),
        ("Gabriel García Márquez", "Colombia")
    ])
    conn.commit()
    conn.close()

init_db()

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.get("/authors")
def get_authors():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, name, country")
    authors = [{"id": r[0], "name": r[1], "country": r[2]} for r in cur.fetchall()]
    conn.close()
    return authors

@app.post("/authors")
def add_author(author: Author):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO authors (name, country) VALUES (?, ?)",
                (author.name, author.country))
    conn.commit()
    conn.close()
    return {"message": "Author added successfully"}

@app.put("/authors/{author_id}")
def update_author(author_id: int, author: Author):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE authors SET name=?, country=? WHERE id=?",
                (author.name, author.country, author_id))
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Author not found")
    conn.commit()
    conn.close()
    return {"message": "Author updated successfully"}

@app.delete("/authors/{author_id}")
def delete_author(author_id: int):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM authors WHERE id=?", (author_id,))
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Author not found")
    conn.commit()
    conn.close()
    return {"message": "Author deleted successfully"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
