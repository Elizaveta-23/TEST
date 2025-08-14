import pandas as pd

orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filtered_orders = orders[(orders['total'] > 10000) & (orders['total'] < 15000) & (orders['order_date'] >= '2023-01-01') & (orders['order_date'] <= '2023-12-31')]
print(filtered_orders[['order_id', 'total', 'order_date']])