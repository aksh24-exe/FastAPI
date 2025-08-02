from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Create or Insert Data
# @app.post("/product")
# async def create_product(new_product: dict):
#     return new_product

# With Pydantic
# Define the Product MOdel
class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None

# @app.post("/product")
# async def create_product(new_product: Product):
#     return new_product


# Access Attribute inside the Function
# @app.post("/product")
# async def create_product(new_product: Product):
#     print(new_product.id)
#     print(new_product.name)
#     print(new_product.price)
#     print(new_product.stock)
#     return new_product

# Add new calculated attributes
# @app.post("/product")
# async def create_product(new_product: Product):
#     product_dict = new_product.model_dump()
#     price_with_tax = new_product.price + (new_product.price * 18/100)

#     product_dict.update({"Price_with_tax": price_with_tax})

#     return product_dict


# Combining Request Body with PAth Parameter
# @app.put("/product/{product_id}")
# async def update_product(product_id: int, new_updated_product: Product):
#     return{"ProductId": product_id,
#            "New_Updated_Product": new_updated_product}

# Adding Query Parameter
@app.put("/product/{product_id}")
async def update_product(product_id: int, new_updated_product: Product, discount: float | None = None):
    return{"ProductId": product_id,
           "New_Updated_Product": new_updated_product, "Discount": discount}