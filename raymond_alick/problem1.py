import time
start = time.time()

import numpy as np
import pandas as pd
import re
from matplotlib import pyplot as plt
plt.style.use('ggplot')

# orders_df=pd.read_csv('Orders.csv', header = None)
orders_df=pd.read_csv('Orders.csv')

# exit()
# orders_df.index
orders_df['Profit'] = orders_df['Profit'].apply(lambda x: x.replace('$', ''))
orders_df['Profit'] = orders_df['Profit'].apply(lambda x: x.replace(',', ''))
orders_df['Profit'] = orders_df['Profit'].apply(lambda x: float(x))

orders_df['Sales'] = orders_df['Sales'].apply(lambda x: x.replace('$', ''))
orders_df['Sales'] = orders_df['Sales'].apply(lambda x: x.replace(',', ''))
orders_df['Sales'] = orders_df['Sales'].apply(lambda x: float(x))

# print ('Execution Time: ', time.time()- start ,' Seconds')
