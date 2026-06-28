from typing import Dict
from fastapi import FastAPI

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