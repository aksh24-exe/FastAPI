from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'mssg': 'Hello Fast API'}