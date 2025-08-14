import pandas as pd

orders = pd.read_csv('orders.csv', sep=',',encoding='utf-8')
filtered_orders = orders[((orders['customer_id']>=10) & (orders['customer_id']<=20) & (orders['total'] > 8000))]
print(filtered_orders[['order_id','customer_id','total']])