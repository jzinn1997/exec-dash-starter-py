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

#original code founded here: https://plot.ly/python/bar-charts/

data = [
    graph_objs.Bar(
        x= [20, 14, 23],
        y= ['mint chocolate chip', 'cookie dough', 'coffee']
        orientation= "h" #horizontal bar graph
    )
]

chart_title = "Top Selling Products (February 2019)" # TODO: get month and year

#orginal code founded here: https://plot.ly/python/getting-started/

chart_options = {
    "data": data,
    "layout": graph_objs.Layout(title="favorite ice cream flavors")
}
plotly.offline.plot(chart_options, auto_open=True)




