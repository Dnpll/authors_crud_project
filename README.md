# 📚 Authors CRUD Application

## 1. Cel systemu

Aplikacja Authors CRUD to prosty system demonstracyjny typu CRUD (Create, Read, Update, Delete), służący do zarządzania danymi autorów literackich.  
System wykorzystuje FastAPI (Python) oraz bazę danych SQLite.  
Interfejs użytkownika został przygotowany w technologii HTML + JavaScript.

---

## 2. Funkcjonalność systemu

System umożliwia:

- Pobieranie listy wszystkich autorów.  
- Dodawanie nowego autora.  
- Edytowanie istniejącego rekordu.  
- Usuwanie autora.  
- Automatyczną inicjalizację bazy z przykładowymi danymi przy pierwszym uruchomieniu.

Każdy autor zawiera następujące pola:

| Pole | Typ | Opis |
|------|------|------|
| name | string | Imię i nazwisko autora |
| country | string | Kraj pochodzenia |
| birth_year | integer | Rok urodzenia |
| bio | string | Krótka biografia |

---
