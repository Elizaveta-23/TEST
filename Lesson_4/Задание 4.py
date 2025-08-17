import pandas as pd

gr_orders = pd.read_csv('group_orders.csv')
gr_orders['order_month'] = pd.to_datetime(gr_orders['order_date'], errors='coerce').dt.strftime('%Y-%m')
gr_orders_month = gr_orders.groupby('order_month')['total'].sum().reset_index(name='month_total')
print(gr_orders_month)