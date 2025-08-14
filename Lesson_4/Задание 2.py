import pandas as pd

gr_orders = pd.read_csv('group_orders.csv', sep=',',encoding='utf-8')
orders_city = gr_orders.groupby('city')['total'].mean().reset_index(name='avg_order_total')
print(orders_city)