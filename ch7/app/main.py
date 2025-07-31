from fastapi import FastAPI

app = FastAPI()

# Order is Important
#  define the type of the product
# Static
# Dynamic
# Order is Important if like this then static first and then after we dynamic operation

@app.get("/product/product_title")
async def  single_product():
    return {"response":"Single Data Fetch",
           }


@app.get("/product/{product_title}")
async def  single_product(product_title: str):
    return {"response":"Single Data Fetch",
            "product_id": product_title}

