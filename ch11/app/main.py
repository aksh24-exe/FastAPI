from fastapi import FastAPI

app = FastAPI()

#single query Parameter
# If we not make a path parameter and give argument to the function then it is Query Paramter
@app.get("/product")
async def product(category: str):
    return {"status": "ok", "Category": category}

#  Mulitiple Query Parameter
@app.get("/product1")
async def product(category: str, limit: int):
    return {"status": "ok", "Category": category, "Limit": limit}

# Default Query Parameter
@app.get("/product3")
async def product(category: str, limit: int=10):
    return {"status": "ok", "Category": category, "Limit": limit}

# Optional Query Paramter
@app.get("/product2")
async def product(category: str, limit: int | None = None):
    return {"status": "ok", "Category": category, "Limit": limit}


@app.get("/product4/{year}")
async def product(year: str, category: str):
    return {"status": "ok", "Category": category, "Year": year}