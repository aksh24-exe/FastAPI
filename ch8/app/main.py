from fastapi import FastAPI
from enum import Enum

app =FastAPI()

## Predifeine Values
# Define an Enum class with allowed product categories
class ProductCategory(str, Enum):
    books = "Books"
    clothings = "Clothings"
    elctronics = "Electronics"


# Use the Enum as the type for the path paramter
# @app.get("/product/{category}")
# async def get_products(category: ProductCategory):
#     return {"response": "Product Fetch",
#             "Category": category}

# Working Pyhton Enum
@app.get("/product/{category}")
async def get_products(category: ProductCategory):
   if category == ProductCategory.books:
       return {"response": "Books are Awesome"}
   elif category == ProductCategory.clothings:
        return {"response": "Awesome Faisone"}
   elif category == ProductCategory.books.value:
       return {"response": "Books are Awesome"}

   return {"response": category}