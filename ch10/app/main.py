from fastapi import FastAPI

app = FastAPI()

PRODUCTS = [
        {
            "id": 1,
            "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
            "price": 109.95,
            "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday"
        },
        {
            "id": 2,
            "title": "Mens Casual Premium Slim Fit T-Shirts ",
            "price": 22.3,
            "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket."
        },
        {
            "id": 3,
            "title": "Mens Cotton Jacket",
            "price": 55.99,
            "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day."
        },
    ]

# GET Request
# Read or Fetch ALL DATA
@app.get("/product")
async def all_product():
    return PRODUCTS

# Read or Fetch All Data
@app.get('/product/{product_id}')
async def single_product(product_id: int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product

# POST Request
# Create or Insert data
@app.post("/product")
async def create_product(new_product: dict):
    PRODUCTS.append(new_product)
    return{"status": "Created", "new_product": new_product}

# PUT Response
## Update Complete Data
@app.put("/product/{product_id}")
async def update_product(product_id: int, new_update_product: dict):
    for index, products in enumerate(PRODUCTS):
        if products["id"] == product_id:
            PRODUCTS[index] = new_update_product
            return {"status": "Updated", "product_id": product_id,
                    "new_product": new_update_product}
        

# PATCH Response
## Updated Partial Data
@app.patch("/product/{product_id}")
async def partial_product(product_id: int, new_updated_product: dict):
    for product in PRODUCTS:
        if product["id"] == product_id:
            product.update(new_updated_product)
            return {"status": "Partrial Updated", "product_id": product_id, "New_product": new_updated_product}
        
# Delete Request
# Delete Data
@app.delete("/product/{product_id}")
async def delete_product(product_id: int):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS.pop(index)
            return {"Response": "product is deleted"}