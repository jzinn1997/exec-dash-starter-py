# monthly_sales.py

import operator
import os
import pandas

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#function from https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(my_price):
    return "${0:,.2f}".format(my_price) 

#
#INPUTS
#

csv_filename = "sales-201803.csv" #TODO: must allow user to specify

#referenced https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md#file-operations
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

#referenced https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/pandas.md
csv_data = pandas.read_csv(csv_filepath)

#
#CALCULATIONS
#

#setting variables

monthly_total = csv_data["sales price"].sum()

product_names = csv_data["product"]
unique_product_names = product_names.unique()
unique_product_names = unique_product_names.tolist()

top_sellers = []

for product_name in unique_product_names:
    matching_rows = csv_data[csv_data["product"] == product_name]
    product_monthly_sales = matching_rows["sales price"].sum()
    top_sellers.append({"name": product_name, "monthly_sales": product_monthly_sales})

top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly_sales"), reverse=True)


#
# OUTPUTS
#

print("-----------------------")
print("MONTH: February 2019") #TODO: Get month and year!!

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")

rank = 1
for d in top_sellers:
    print("  " + str(rank) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))
    rank = rank + 1

print("-----------------------")
print("VISUALIZING THE DATA...")


chart_title = "Top Selling Products (February 2019)" # TODO: get month and year

sorted_names = []
sorted_sales = []

for d in top_sellers:
    sorted_names.append(d["name"])
    sorted_sales.append(d["monthly_sales"])

#display top-sellers at top
sorted_names.reverse()
sorted_sales.reverse()

#customize the graph - original code from professor rossetti
fig, ax = plt.subplots()
usd_formatter = ticker.FormatStrFormatter('$%1.0f')
ax.xaxis.set_major_formatter(usd_formatter)

#nuts and bolts of the chart
plt.barh(sorted_names, sorted_sales)
plt.title(chart_title)
plt.xlabel("Product")
plt.ylabel("Monthly Sales (USD)")

#fixes labels getting cut off
plt.tight_layout()
plt.show()

