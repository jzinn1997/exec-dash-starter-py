# monthly_sales.py

# TODO: import some modules and packages here

import os
import pandas

def to_usd(my_price):
    return "${0:,.2f}".format(my_price) 

#INPUTS

csv_filename = "sales-201803.csv" #must allow user to specify
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)
csv_data = pandas.read_csv(csv_filepath)

#print(type(cvs_data))
#print(list(csv_data.columns))

#
#CALCULATIONS
#

monthly_total = csv_data["sales price"].sum()

product_totals = csv_data.groupby(["product"]).sum()
product_totals = product_totals.sort_values("sales price", ascending=False)

#products_sold = csv_data["product"].unique()
#products_sold = products_sold.tolist()


#for product_name in products_sold:
 #   print(product_name)
    # breakpoint()

top_sellers = [
    {"rank": 1, "name": "Button-Down Shirt", "monthly_sales": 6960.35},
    {"rank": 2, "name": "Super Soft Hoodie", "monthly_sales": 1875.00},
]
# get above information from csv_data



# OUTPUTS


print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))
print("-----------------------")
print("VISUALIZING THE DATA...")
