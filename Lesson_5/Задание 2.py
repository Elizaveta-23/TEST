import pandas as pd

orders = pd.read_csv('orders_new.csv')

orders['total'] = orders['price'] * orders['quantity']
mask_query = orders.query('product == "C" and total > 250')
print(mask_query)