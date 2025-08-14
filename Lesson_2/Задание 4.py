import pandas as pd

customers = pd.read_csv('customers.csv', sep=',',encoding='utf-8')
filtered_customers = customers[(customers['gender'] == 'F') & (customers['birth_date'] < '1995-01-01')]
print(filtered_customers[['customer_id', 'first_name', 'last_name', 'birth_date']])