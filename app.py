from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# PostgreSQL database
# Format: postgresql://<username>:<password>@<host>:<port>/<database_name>
# Change the values below to match your local PostgreSQL setup,
# or set the DATABASE_URL environment variable instead.
DB_USERNAME = os.environ.get('DB_USERNAME', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'your_password')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'employee_db')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ---------------- MODEL ----------------
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "salary": self.salary,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }


# Create tables if they don't exist
with app.app_context():
    db.create_all()


# ---------------- ROUTES ----------------

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Employee CRUD API is running"})


# CREATE
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()

    if not data or not all(k in data for k in ("name", "email", "department", "salary")):
        return jsonify({"error": "name, email, department and salary are required"}), 400

    if Employee.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Employee with this email already exists"}), 409

    new_employee = Employee(
        name=data['name'],
        email=data['email'],
        department=data['department'],
        salary=data['salary']
    )
    db.session.add(new_employee)
    db.session.commit()

    return jsonify(new_employee.to_dict()), 201


# READ ALL
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([emp.to_dict() for emp in employees]), 200


# READ ONE
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(employee.to_dict()), 200


# UPDATE
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    employee.name = data.get('name', employee.name)
    employee.email = data.get('email', employee.email)
    employee.department = data.get('department', employee.department)
    employee.salary = data.get('salary', employee.salary)

    db.session.commit()
    return jsonify(employee.to_dict()), 200


# DELETE
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": f"Employee {employee_id} deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
