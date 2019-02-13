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

print(product_totals)
#                     unit price  units sold  sales price
#product
#Button-Down Shirt     1821.40         107      6960.35
#Super Soft Hoodie     1350.00          25      1875.00
#Khaki Pants           1157.00          18      1602.00
#Vintage Logo Tee       398.75          59       941.05
#Brown Boots            250.00           2       250.00
#Sticker Pack           108.00          48       216.00
#Baseball Cap           156.31           7       156.31

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


#need to display bar chart of top sellers

