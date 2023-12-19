import pytest
from my_app.main import create_employee

def test_create_employee_id():
    employee = create_employee()
    assert isinstance(employee["id"], int)
    assert 1000 <= employee["id"] <= 9999

def test_create_employee_name():
    employee = create_employee()
    assert isinstance(employee["name"], str)
    assert len(employee["name"]) > 0

def test_create_employee_address():
    employee = create_employee()
    assert isinstance(employee["address"], str)
    assert len(employee["address"]) > 0

def test_create_employee_email():
    employee = create_employee()
    assert isinstance(employee["email"], str)
    assert "@" in employee["email"]

def test_create_employee_job_title():
    employee = create_employee()
    assert isinstance(employee["job_title"], str)
    assert len(employee["job_title"]) > 0
