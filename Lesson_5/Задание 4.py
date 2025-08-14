import pandas as pd

users = pd.read_csv('users_new.csv')
orders = pd.read_csv('orders_new.csv')

df = orders.merge(users, on='user_id', how='inner')

df['total'] = df['price'] * df['quantity']
mask_table = df.pivot_table(index='region', columns='product', values='total', aggfunc='sum')
print(mask_table)