# monthly_sales.py

import os
import pandas
import plotly
from plotly import graph_objs


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
product_totals = csv_data.groupby(["product"]).sum()
product_totals = product_totals.sort_values("sales price", ascending=False)

top_sellers = []
rank = 1
for i, row in product_totals.iterrows():
    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
    top_sellers.append(d)
    rank = rank + 1


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
for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))


print("-----------------------")
print("VISUALIZING THE DATA...")


chart_filename = "top-sellers-201803.html" 
chart_filepath = os.path.join(os.path.dirname(__file__), "reports", chart_filename)

#image_filename = "top-sellers-201803.png" # TODO: parse selected csv file name
#image_filepath = os.path.join(os.path.dirname(__file__), "images", image_filename) # looks like the image just gets downloaded
#image_filename = "top-sellers-201803" # TODO: parse selected csv file name



#original code founded here: https://plot.ly/python/bar-charts/
#breakpoint()
sorted_product_sales = [d["monthly_sales"] for d in top_sellers]   
sorted_product_names = [d["name"] for d in top_sellers]

x=sorted_product_sales
y=sorted_product_names

data = [
    graph_objs.Bar(
        x=x,
        y=y,
        orientation = 'h' 
    )
]

chart_title = "Top Selling Products (February 2019)" # TODO: get month and year

#orginal code founded here: https://plot.ly/python/getting-started/

layout = graph_objs.Layout(
    title=chart_title,
    yaxis=dict(autorange="reversed") # make sure top sellers are on the top
)

chart_options = {"data": data, "layout": layout}

chart_options = {
    "data": data,
    "layout": graph_objs.Layout(title="Top Selling Products (February 2019)")
}
plotly.offline.plot(chart_options, auto_open=True)


plotly.offline.plot(
    chart_options,
    filename=chart_filepath,
    #image="png",
    #image_filename=image_filename, #specify filepath???????
    auto_open=True
)

print("-----------------------")
print("SEE: " + chart_filepath)

