import pandas as pd

contacts = pd.read_csv('contacts.csv', sep=',', encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',', encoding='utf-8')
orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')

merged_2 = orders.merge(customers, on='customer_id', how='inner').merge(contacts, on='customer_id', how='inner')
merged_2["order_date"] = pd.to_datetime(merged_2["order_date"], errors='coerce')
merged_2["registration_date"] = pd.to_datetime(merged_2["registration_date"], errors='coerce')

query_2 = merged_2.query('registration_date.dt.year >= 2022 and order_date.dt.year == 2023 and total > 30000')
print(query_2[['first_name', 'last_name','total']])
print(f"Количество продаж: {len(query_2)}")