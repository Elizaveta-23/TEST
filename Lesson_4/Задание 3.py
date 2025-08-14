import pandas as pd

gr_orders = pd.read_csv('group_orders.csv', sep=',',encoding='utf-8')
gr_orders_most = gr_orders.groupby('product')['quantity'].sum().reset_index(name='sum_quantity')
print(gr_orders_most.sort_values('sum_quantity', ascending=False, ignore_index=True).head(1))