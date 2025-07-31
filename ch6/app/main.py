from fastapi import FastAPI

app = FastAPI()

# ## Parameter with type
# # Not define the type of the product
# @app.get("/product/{product_is}")
# async def  single_product(product_id):
#     return {"response":"Single Data Fetch",
#             "product_id": product_id}

## Parameter with type
#  define the type of the product
@app.get("/product/{product_is}")
async def  single_product(product_id: int):
    return {"response":"Single Data Fetch",
            "product_id": product_id}

## Parameter with type
#  define the type of the product
@app.get("/product/{product_title}")
async def  single_product(product_title: str):
    return {"response":"Single Data Fetch",
            "product_id": product_title}