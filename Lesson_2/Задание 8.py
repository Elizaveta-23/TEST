import pandas as pd

orders = pd.read_csv('orders.csv', sep=',', encoding='utf-8')
filter_orders = orders[(orders['total'] > 5000) & (orders['order_date'] >= '2023-02-01') & (orders['order_date'] <= '2023-02-29')]
print(filter_orders[['order_id', 'total', 'order_date']])