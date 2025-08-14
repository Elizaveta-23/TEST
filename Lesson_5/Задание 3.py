import pandas as pd

orders = pd.read_csv('orders_new.csv')
mask_vc = orders['product'].value_counts().reset_index(name='order_count')
print(mask_vc)