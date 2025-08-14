import pandas as pd

group_orders = pd.read_csv('group_orders.csv')
group_orders_city = group_orders.groupby('city')['order_id'].count().reset_index(name='total_orders')
print(group_orders_city)