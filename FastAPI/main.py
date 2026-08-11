from fastapi import FastAPI

import random


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/random-number/{max_value}")
def get_random_number(max_value: int):
    return {
        "max": max_value,
        "random_number": random.randint(1, max_value)
    }