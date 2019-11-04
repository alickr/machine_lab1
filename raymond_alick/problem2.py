try:
    from problem1 import orders_df as orders_df
except ImportError:
    print ('Error! Importing problem1.py failed')
    exit()

import datetime

print(orders_df.groupby('Sales'))

print(type(orders_df['Order.Date']))

orders_df['Month'] = orders_df['Order.Date'].apply(lambda x: datetime.datetime.strptime(x, "%m/%d/%y").strftime('%B'))
# print(orders_df['month'])
# print(orders_df)
# trends_df = orders_df.groupby(['Month','Category']).['Month'].sort()
category_trends_df = orders_df.groupby(['Month','Category'])['Quantity'].count()
# category_trends_df = orders_df.groupby(['Month','Category'])['Quantity'].count()

# category_trends_df = category_trends_df.assign(sales = lambda x: np.mean(x.sales))
# category_trends_df = category_trends_df.apply(sales = lambda x: np.mean(x.sales))

print(category_trends_df)





# print ('Execution Time: ', time.time()- start ,' Seconds')
