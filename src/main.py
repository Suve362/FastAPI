from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/hello")
def get_hello(name: str):
    return f"Hello, {name}!"