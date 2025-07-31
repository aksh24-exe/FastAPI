from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'mssg': 'Hello Fast API'}

# GET Request
# Read or Fetch All Dtaa
@app.get("/product")
async def all_products():
    return {"response": "Hello From the Products"}

# Read or Fetch single Dtaa
@app.get("/product/{product_id}")
async def all_products(product_id: int):
    return {"response": "Hello From the Products",
            "product_is": product_id}

# Post
# Create or Insert Data
@app.post("/product")
async def create_product(product: dict):
    return {"response": "Products Created",
            "product_is": product}

# Put
# Update Complete Data
@app.put("/product/{product_id}")
async def update_product(new_updated_product: dict, product_id: int):
    return {"response":"Complete Data Updated",
            "Product_Id": product_id,
            "Updated_Product": update_product}

# Patch
# Update Partial Data
@app.patch("/product/{product_id}")
async def partial_product(new_updated_product: dict, product_id: int):
    return {"response":"Complete Data Updated",
            "Product_Id": product_id,
            "Updated_Product": update_product}

# Delete
# Delete Data
@app.delete('/product/{product_id}')
async def delete_product(product_id: int):
    return {"response": "Product is Deleted",
            "prodct_id": product_id}