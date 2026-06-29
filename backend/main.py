from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to DevPilot AI"
    }


@app.get("/about")
def about():
    return {
        "developer": "Satya",
        "course": "Learning Full Stack Development"
    }

@app.get("/contact")
def contact():
    return {
    "email":"satya@example.com",
    "phone":"9999999999"
    }

@app.get("/skills")
def skills():
    return {
    "skills":[
        "Linux",
        "AWS",
        "Azure",
        "Kubernetes",
        "Terraform"
    ]
    }
@app.get("/hello/{name}")
def hello(name: str):
    return {
        "message": f"Hello {name}"
    }

@app.get("/search")
def search(query: str):
    return {
        "search": f"{query}"
    }

class Employee(BaseModel):
    name: str
    age: int
    city: str

@app.post("/register")
def create_employee(employee: Employee):
    return {
        "message": "Employee Created Succesfully",
        "employee": {
            name: employee.name,
            age: employee.age,
            city: employee.city
        }
    }
