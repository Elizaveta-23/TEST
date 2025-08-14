import pandas as pd

customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

merged_3 = orders.merge(customers, on='customer_id', how='inner')
merged_3["order_date"] = pd.to_datetime(merged_3["order_date"], errors='coerce')

filter_3 = merged_3.query('gender in ["M", "F"] and 2022 <= order_date.dt.year <= 2023')
print(filter_3['gender'].value_counts())