from flask import Flask, render_template, redirect, url_for
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

# Function to generate fake employee data
def create_employee():
    return {
        "id": random.randint(1000, 9999),
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "job_title": fake.job()
    }

# In-memory list to hold employees
employees = [create_employee() for _ in range(10)]

# Route to display a list of employees
@app.route('/')
def index():
    return render_template('index.html', employees=employees)

# Route to add a new employee and redirect to index
@app.route('/add-employee', methods=['GET'])
def add_employee():
    employees.append(create_employee())
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 
