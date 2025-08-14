import pandas as pd

orders = pd.read_csv('orders.csv', sep=',',encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',',encoding='utf-8')
contacts = pd.read_csv('contacts.csv', sep=',',encoding='utf-8')
merged = customers.merge(orders, on='customer_id',how='inner').merge(contacts, on='customer_id',how='inner')
print(merged)

merged["order_date"] = pd.to_datetime(merged["order_date"], errors='coerce')
desired_countries = ["Italy", "Spain", "UK", "France", "Germany", "Russia"]

filter_1 = merged[(merged['country'].isin(desired_countries)) & (merged['order_date'] >= "2023-01-01") & (merged['order_date'] <= "2023-06-30")]
print(filter_1[['total', 'order_id']])
print(f"Total sum = {filter_1['total'].sum()}")

filter_loc = merged.loc[(merged['order_date'].dt.year == 2023) & (merged['order_date'].dt.month <=6) & (merged['country'].isin(desired_countries))]
print(filter_loc[['total', 'order_id']])
print(f"Total sum = {filter_loc['total'].sum()}")

filter_query = merged.query('country in @desired_countries and order_date.dt.year == 2023 and order_date.dt.quarter <= 2')
print(filter_query[['total', 'order_id']])
print(f"Total sum = {filter_query['total'].sum()}")