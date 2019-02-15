# monthly_sales.py

import operator
import os
import pandas
import csv

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


#function from https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(my_price):
    return "${0:,.2f}".format(my_price) 

#
#INPUTS
#


#adapted from https://github.com/carolinefeeney/exec-dash-project/blob/master/monthly_sales.py#L144
path = os.path.join("data")
directory = os.listdir(path)

chosen_file = []
while True:
    file_name = input("Please specify a file name: ")
    if file_name in directory:
        chosen_file.append(file_name)
        break
    else:
        print("Sorry! This file name was not found.") 
        continue

csv_filename = file_name 
csv_filepath = os.path.join("data", csv_filename)

#referenced https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/pandas.md
csv_data = pandas.read_csv(csv_filepath)

#
#CALCULATIONS
#

#setting variables
#referenced: https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales_alt.py

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

#dates adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/pandas_explore.py
def month_lookup(month):
	year_month={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return year_month[month]

month = month_lookup(csv_filename[-6:-4])
year = int(csv_filename[6:10]) 

print("-----------------------")
print(("MONTH: ") + str(month) + (" ")+ str(year))

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS: ")

#referenced: https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales_alt.py
rank = 1
for d in top_sellers:
    print("  " + str(rank) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))
    rank = rank + 1

print("-----------------------")
print("VISUALIZING THE DATA...")


chart_title = ("Top Selling Products (")+ str(month) + (" ") + str(year) + (")")

sorted_names = []
sorted_sales = []

for d in top_sellers:
    sorted_names.append(d["name"])
    sorted_sales.append(d["monthly_sales"])

#display top-sellers at top
#referenced: https://georgetown-opim-py.slack.com/messages/CFZDKNKA4/
sorted_names.reverse()
sorted_sales.reverse()

#customize the graph 
#adapted from https://stackoverflow.com/questions/38152356/matplotlib-dollar-sign-with-thousands-comma-tick-labels
fig, ax = plt.subplots()
usd_formatter = ticker.FormatStrFormatter('$%1.0f')
ax.xaxis.set_major_formatter(usd_formatter)

#nuts and bolts of the chart
plt.barh(sorted_names, sorted_sales)
plt.title(chart_title)
plt.ylabel("Product")
plt.xlabel("Monthly Sales (USD)")

#fixes labels getting cut off
#referenced: https://georgetown-opim-py.slack.com/messages/CFZDKNKA4/
plt.tight_layout()
plt.show()

