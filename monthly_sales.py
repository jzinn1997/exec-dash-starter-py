# monthly_sales.py

# TODO: import some modules and packages here

import os
import pandas

def to_usd(my_price):
    return "${0:,.2f}".format(my_price) 

#INPUTS

csv_filename = "sales-201803.csv"
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)
csv_data = pandas.read_csv(csv_filepath)


# TODO: write some Python code here to produce the desired functionality...

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")
