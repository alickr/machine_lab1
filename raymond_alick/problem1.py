import time
start = time.time()

import numpy as np
import pandas as pd
import re
from matplotlib import pyplot as plt
plt.style.use('ggplot')

# data_df=pd.read_csv('Orders.csv', header = None)
data_df=pd.read_csv('Orders.csv')

# exit()
# data_df.index
data_df['Profit'] = data_df['Profit'].apply(lambda x: x.replace('$', ''))
data_df['Profit'] = data_df['Profit'].apply(lambda x: x.replace(',', ''))
data_df['Profit'] = data_df['Profit'].apply(lambda x: float(x))

data_df['Sales'] = data_df['Sales'].apply(lambda x: x.replace('$', ''))
data_df['Sales'] = data_df['Sales'].apply(lambda x: x.replace(',', ''))
data_df['Sales'] = data_df['Sales'].apply(lambda x: float(x))

# print ('Execution Time: ', time.time()- start ,' Seconds')
