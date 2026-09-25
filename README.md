# Employee CRUD API

A simple CRUD (Create, Read, Update, Delete) REST API built with Flask and Flask-SQLAlchemy, using a PostgreSQL database.

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
- Psycopg2

## Project Structure

```text
employee-crud-postgresql/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

### 1. Install PostgreSQL

Make sure PostgreSQL is installed and running on your computer.

### 2. Create the Database

Create the database using PostgreSQL or pgAdmin:

```sql
CREATE DATABASE employee_db;
```

### 3. Create a Virtual Environment

```powershell
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

### 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 5. Configure Database

Set your PostgreSQL database details using environment variables.

For Windows PowerShell:

```powershell
$env:DB_USERNAME="postgres"
$env:DB_PASSWORD="your_password"
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="5432"
$env:DB_NAME="employee_db"
```

> Never commit your real database password to GitHub.

### 6. Run the Application

```powershell
python app.py
```

The API will run at:

```text
http://127.0.0.1:5000/
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/employees` | Create a new employee |
| GET | `/employees` | Get all employees |
| GET | `/employees/<id>` | Get employee by ID |
| PUT | `/employees/<id>` | Update employee by ID |
| DELETE | `/employees/<id>` | Delete employee by ID |

## Sample Request Body

For `POST /employees`:

```json
{
    "name": "Varsha",
    "email": "varsha@example.com",
    "department": "QA",
    "salary": 30000
}
```

For `PUT /employees/<id>`:

```json
{
    "salary": 35000
}
```

## Database

The application uses PostgreSQL with Flask-SQLAlchemy.

The `employee` table contains:

- `id`
- `name`
- `email`
- `department`
- `salary`
- `created_at`

## CRUD Operations

| Operation | HTTP Method | Endpoint |
|-----------|-------------|----------|
| Create | POST | `/employees` |
| Read All | GET | `/employees` |
| Read One | GET | `/employees/<id>` |
| Update | PUT | `/employees/<id>` |
| Delete | DELETE | `/employees/<id>` |

## Pushing Changes to GitHub

After making changes to the README:

```powershell
git add .
git commit -m "Update README for PostgreSQL"
git push
```
