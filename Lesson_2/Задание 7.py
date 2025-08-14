import pandas as pd

customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
merged = orders.merge(customers, on='customer_id', how='inner')
filter_mrg = merged[(merged['birth_date'] >= '1990-01-01') & (merged['birth_date'] <= '1990-12-31')]
print(filter_mrg[['order_id', 'customer_id']])