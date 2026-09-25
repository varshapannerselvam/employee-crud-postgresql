# Employee CRUD API

A simple CRUD (Create, Read, Update, Delete) REST API built with Flask and SQLAlchemy, using a SQLite database.

## Features
- Create an employee
- Get all employees
- Get one employee by ID
- Update an employee
- Delete an employee

## Tech Stack
- Python
- Flask
- Flask-SQLAlchemy
- PostgreSQL

## Setup

1. Make sure PostgreSQL is installed and running on your machine.

2. Create the database (run this once, in `psql` or pgAdmin):
   ```sql
   CREATE DATABASE employee_db;
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set your database credentials. Either edit the `DB_USERNAME` / `DB_PASSWORD` /
   `DB_HOST` / `DB_PORT` / `DB_NAME` defaults directly in `app.py`, or set
   environment variables before running (recommended so you never commit a
   real password):
   ```
   export DB_USERNAME=postgres
   export DB_PASSWORD=your_actual_password
   export DB_NAME=employee_db
   ```
   (On Windows, use `set` instead of `export`.)

6. Run the app:
   ```
   python app.py
   ```

The API will run at `http://127.0.0.1:5000/`

## API Endpoints

| Method | Endpoint              | Description            |
|--------|-----------------------|-------------------------|
| GET    | /                      | Health check            |
| POST   | /employees             | Create a new employee   |
| GET    | /employees             | Get all employees       |
| GET    | /employees/<id>        | Get employee by ID      |
| PUT    | /employees/<id>        | Update employee by ID   |
| DELETE | /employees/<id>        | Delete employee by ID   |

### Sample request body (POST / PUT)
```json
{
  "name": "Varsha",
  "email": "varsha@example.com",
  "department": "QA",
  "salary": 30000
}
```

## Pushing to GitHub

1. Create a new repository on GitHub (don't initialize with a README).
2. In this project folder, run:
   ```
   git init
   git add .
   git commit -m "Employee CRUD API with Flask and SQLAlchemy"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```
