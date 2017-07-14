#from IPython import embed
import csv

products_csv = "data/products.csv"

#
# READ PRODUCTS FROM FILE
#

products = []
with open(products_csv, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for ordered_dict in reader:
        products.append(dict(ordered_dict))

print(products)

#
# HANDLE USER INPUT
#

menu = """
-----------------------------------
PRODUCTS INVENTORY APPLICATION
-----------------------------------

Welcome {0}!

There are {1} products in the database.

    operation | description
    --------- | ------------------
    'Create'  | Add a new product.
    'Read'    | Show information about a product.
    'Update'  | Edit an existing product.
    'Destroy' | Delete an existing product.

Please select an operation: """.format("@s2t2", len(products)) # end of multi- line string. also using string interpolation

crud_operation = input(menu)

def create_product():
    print("CREATING PRODUCT HERE")

def read_product():
    print("READING PRODUCT HERE")

def update_product():
    print("UPDATING PRODUCT HERE")

def destroy_product():
    print("DESTROYING PRODUCT HERE")

if crud_operation.title() == "Create":
    create_product()
elif crud_operation.title() == "Read":
    read_product()
elif crud_operation.title() == "Update":
    update_product()
elif crud_operation.title() == "Destroy":
    destroy_product()
else:
    print("OOPS SORRY. PLEASE TRY AGAIN.")

#
# WRITE PRODUCTS TO FILE
#

with open(products_csv, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=[
      "product_id",
      "product_name",
      "aisle_id",
      "aisle",
      "department_id",
      "department",
      "price"
    ])
    writer.writeheader()

    for product in products:
        writer.writerow(product)
