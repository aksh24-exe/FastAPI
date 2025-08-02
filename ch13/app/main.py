from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import AfterValidator

app =FastAPI()

PRODUCTS = [
{"id": 1, "title": "Ravan Backpack", "price": 109.95,"description": "Perfect for everyday use and forest walks."},
{"id": 2, "title": "Slim Fit T-Shirts", "price": 22.3,"description": "Comfortable, slim-fitting casual shirts."},
{"id": 3, "title": "Cotton Jacket", "price": 55.99,"description": "Great for outdoor activities and gifting."},
]


# Basic Query Parameter
# @app.get("/products")
# async def get_products(search: str | None = None):
#     if search: 
#         search_lower = search.lower()
#         filter_product = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filter_product.append(product)
#         return filter_product
#     return PRODUCTS


# Validation without Annotated
# @app.get("/products")
# async def get_products(search: str | None = Query(default=None, max_length=5, min_length=3)):
#     if search: 
#         search_lower = search.lower()
#         filter_product = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filter_product.append(product)
#         return filter_product
#     return PRODUCTS


#  Valiadtion Throught Annotated
# Follow this Process
# @app.get("/products")
# async def get_products(
#     search: 
#     Annotated[
#         str | None , 
#         Query(max_length=5, min_length=3)
#         ] = None):
#     if search: 
#         search_lower = search.lower()
#         filter_product = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filter_product.append(product)
#         return filter_product
#     return PRODUCTS


# Why use Annotated

## Clear separation of the type
## Better support in some editors and tools for showing metadata and validations directly in the type hints
## Requires Python 3.9+ and FastAPI 0.95+; more modern and recommended approach
## FastAPI 0.95+ officially recommends using Annotated for dependencies and parameters

# Required Parametr
# @app.get("/products")
# async def get_products(
#     search: 
#     Annotated[
#         str | None , 
#         Query(max_length=5, min_length=3)
#         ] ):
#     if search: 
#         search_lower = search.lower()
#         filter_product = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filter_product.append(product)
#         return filter_product
#     return PRODUCTS

# Add regular Experation
# @app.get("/products")
# async def get_products(
#     search: 
#     Annotated[
#         str | None , 
#         Query(max_length=5, min_length=3, pattern="^[s-z]+$")
#         ] ):
#     if search: 
#         search_lower = search.lower()
#         filter_product = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filter_product.append(product)
#         return filter_product
#     return PRODUCTS

# # # Mulitiple Search Team (List)
# @app.get("/products")
# async def get_products(search: Annotated[list[str] | None, Query(min_length=1)] = None):
#     if search:
#         filter_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filter_products.append(product)
#         return filter_products
#     return PRODUCTS


# Alias Paramert
# Change the name of search to q
# @app.get("/products")
# async def get_products(search: Annotated[list[str] | None, Query(min_length=1, alias="q")] = None):
#     if search:
#         filter_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filter_products.append(product)
#         return filter_products
#     return PRODUCTS



# Add MetaData
# @app.get("/products")
# async def get_products(search: Annotated[list[str] | None, Query(min_length=1, title="Search Products", description="Search by Product Title")] = None):
#     if search:
#         filter_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filter_products.append(product)
#         return filter_products
#     return PRODUCTS

# Deprecated True
# @app.get("/products")
# async def get_products(search: Annotated[list[str] | None, Query(min_length=1, title="Search Products", description="Search by Product Title", deprecated=True)] = None):
#     if search:
#         filter_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filter_products.append(product)
#         return filter_products
#     return PRODUCTS


# Custom Validation
def check_valid_id(id: str):
    if not id.startswith("prod-"):
        raise ValueError("Id must Start with 'prod-'")
    return id

@app.get("/products/")
async def get_products(id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
    if id:
        return {"ID": id, "Message": "Valid ID Product"}
    return {"mssg": "Not Proper Id"}
