import pandas as pd

orders = pd.read_csv('orders.csv', sep=',',encoding='utf-8')
filtered_orders = orders[((orders['total']>=30000) & (orders['total']<=40000))]
filtered_orders = filtered_orders[filtered_orders['order_date'] >= '2023-01-01']
print(filtered_orders['order_id'])
