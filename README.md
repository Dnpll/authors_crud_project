# Author CRUD API

Prosty projekt demonstracyjny stworzony w Python (FastAPI + SQLite), pokazujący pełny CRUD (Create, Read, Update, Delete) dla encji **Author**.

---

## Technologie

- **Backend:** FastAPI, SQLAlchemy, Pydantic  
- **Baza danych:** SQLite  
- **Frontend:** prosty HTML + Fetch API  
- **API:** REST

---

## Wprowadzone zmiany

W ramach rozszerzenia projektu dodano dwa nowe pola w encji **Author**:  
- **biography (TEXT)** — krótka informacja biograficzna o autorze  
- **birth_year (INTEGER)** — rok urodzenia autora  

Zaktualizowano:
- model bazy danych (SQLite)  
- endpointy API (GET, POST, PUT, DELETE)  
- frontend (formularz HTML i lista autorów)  

---

## render.com

1. Utwórzyć nowy projekt na [render.com](https://render.com)  
2. Podłączyć repozytorium z tym projektem  
3. Uruchomić projekt  

Aplikacja dostępna pod adresem:  
[https://authors-crud-project-1.onrender.com/](https://authors-crud-project-1.onrender.com/)
