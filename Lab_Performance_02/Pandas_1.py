import pandas as pd

data_f = pd.read_csv("H:\AI_Lab\CLP_Code\Lab_Manual_2\KaiSed_Sheet - 1.csv")

print(data_f.head())

total_revenue_per_product = data_f.groupby("Product")["Revenue"].sum()

print("Total Revenue Per Product Are Given Below: \n",total_revenue_per_product)
