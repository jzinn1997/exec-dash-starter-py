# monthly_sales.py

import operator
import os
import pandas

import matplotlib.pyplot as plt

import matplotlib.ticker as ticker


def to_usd(my_price):
    return "${0:,.2f}".format(my_price) 

#
#INPUTS
#

csv_filename = "sales-201803.csv" #TODO: must allow user to specify
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)
csv_data = pandas.read_csv(csv_filepath)

#original formulas found on prof rossetti github

#
#CALCULATIONS
#

#setting variables

monthly_total = csv_data["sales price"].sum()
#product_totals = csv_data.groupby(["product"]).sum()
#product_totals = product_totals.sort_values("sales price", ascending=False)

#this was using plotly
#top_sellers = []
#rank = 1
#for i, row in product_totals.iterrows():
#    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
#    top_sellers.append(d)
#    rank = rank + 1

#switching to matplotlib

product_names = csv_data["product"]

unique_product_names = product_names.unique()

unique_product_names = unique_product_names.tolist()

#top_sellers = [
#    {"name": "Button-Down Shirt", "monthly_sales": 6960.34},
#    {"name": "Super Soft Hoodie", "monthly_sales": 1875.0},
#    {"name": "Khaki Pants", "monthly_sales": 1602.0},
#    {"name": "Vintage Logo Tee", "monthly_sales": 941.05},
#    {"name": "Brown Boots", "monthly_sales": 250.0},
#    {"name": "Sticker Pack", "monthly_sales": 216.0},
#    {"name": "Baseball Cap", "monthly_sales": 156.31}   
#]

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


#chart_filename = "top-sellers-201803.html" 
#chart_filepath = os.path.join(os.path.dirname(__file__), "reports", chart_filename)

#image_filename = "top-sellers-201803.png" # TODO: parse selected csv file name
#image_filepath = os.path.join(os.path.dirname(__file__), "images", image_filename) # looks like the image just gets downloaded
#image_filename = "top-sellers-201803" # TODO: parse selected csv file name



#original code founded here: https://plot.ly/python/bar-charts/
#breakpoint()
#sorted_sales = [d["monthly_sales"] for d in top_sellers]   
#sorted_names = [d["name"] for d in top_sellers]
#
#x=sorted_sales
#y=sorted_names

#data = [
#    graph_objs.Bar(
#        x=x,
#        y=y,
#        orientation = 'h' 
#    )
#]

chart_title = "Top Selling Products (February 2019)" # TODO: get month and year

sorted_names = []
sorted_sales = []

for d in top_sellers:
    sorted_names.append(d["name"])
    sorted_sales.append(d["monthly_sales"])


sorted_names.reverse()
sorted_sales.reverse()

#customize the graph - original code from professor rossetti
fig, ax = plt.subplots()
usd_formatter = ticker.FormatStrFormatter('$%1.0f')
ax.xaxis.set_major_formatter(usd_formatter)

plt.barh(sorted_names, sorted_sales)
plt.title(chart_title)
plt.xlabel("Product")
plt.ylabel("Monthly Sales (USD)")

#trying to fix labels getting cut off
plt.tight_layout()
plt.show()



#orginal code founded here: https://plot.ly/python/getting-started/

# layout = graph_objs.Layout(
    #title=chart_title,
    #yaxis=dict(autorange="reversed") # make sure top sellers are on the top
# 
# 
# chart_options = {"data": data, "layout": layout}
# 
# chart_options = {
#    "data": data,
#    "layout": graph_objs.Layout(title="Top Selling Products (February 2019)")
# 
# plotly.offline.plot(chart_options, auto_open=True)
# 
# 
# plotly.offline.plot(
#    chart_options,
#    filename=chart_filepath,
#    #image="png",
#    #image_filename=image_filename, #specify filepath???????
#    auto_open=True
# 

#print("-----------------------")
#print("SEE: " + chart_filepath)

