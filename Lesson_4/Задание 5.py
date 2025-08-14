import pandas as pd

gr_orders = pd.read_csv('group_orders.csv')
gr_orders_mean = gr_orders.groupby('city')['total'].mean().reset_index(name='mean_total')
print(gr_orders_mean.sort_values('mean_total', ascending=False).head(3))