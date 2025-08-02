from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()
PRODUCTS = [
{"id": 1, "title": "Ravan Backpack", "price": 109.95,"description": "Perfect for everyday use and forest walks."},
{"id": 2, "title": "Slim Fit T-Shirts", "price": 22.3,"description": "Comfortable, slim-fitting casual shirts."},
{"id": 3, "title": "Cotton Jacket", "price": 55.99,"description": "Great for outdoor activities and gifting."},
]

# Basic Path Parameter
# @app.get("/products/{product_id}")
# async def get_product(product_id: int):
#     if product_id:
#         for product in PRODUCTS:
#             if product["id"] == product_id:
#                 return {"Message": "Done", "Product": product}
#         return {"Message": "Not find the Product"}

# Numerice Valiadtion
# @app.get("/products/{product_id}")
# async def get_product(product_id: Annotated[int, Path(ge=1, le=3)]):
#     if product_id:
#         for product in PRODUCTS:
#             if product["id"] == product_id:
#                 return {"Message": "Done", "Product": product}
#         return {"Message": "Not find the Product"}

# Adding meta data
# @app.get("/products/{product_id}")
# async def get_product(product_id: Annotated[int, Path(ge=1, le=3, title="Give the Product id", description="All Product details")]):
#     if product_id:
#         for product in PRODUCTS:
#             if product["id"] == product_id:
#                 return {"Message": "Done", "Product": product}
#         return {"Message": "Not find the Product"}

# Combining Path and Query Paramter
@app.get("/product/{product_id}")
async def get_product(product_id: Annotated[int, Path( gt=0, le=100)], search:Annotated[str | None, Query( max_length=20)] = None ):
    for product in PRODUCTS:
        if product["id"] == PRODUCTS:
            if search and search.lower() not in product["title"].lower():
                return {"Error": "Product not match the search tearm"}
            return product
    return {"Error": "Product not Found"}