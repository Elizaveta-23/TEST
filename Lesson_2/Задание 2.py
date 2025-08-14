import pandas as pd

orders = pd.read_csv('orders.csv', sep=',',encoding='utf-8')
filtered_orders = orders[((orders['customer_id']>=68) & (orders['customer_id']<=88))]
filtered_orders = filtered_orders[(filtered_orders['order_date'] >= '2022-01-01') & (filtered_orders['order_date'] <= '2022-12-31')]
print(filtered_orders[5:11][['order_id','total']])