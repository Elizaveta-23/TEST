import pandas as pd

orders = pd.read_csv('products.csv', sep=',',encoding='utf-8')
filtered_orders = orders[orders['price']<=500]
filtered_orders = filtered_orders[filtered_orders['volume_ml']==5]
print(filtered_orders[['product_name','price']])