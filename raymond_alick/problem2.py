try:
    from problem1 import orders_df as orders_df
except ImportError:
    print ('Error! Importing problem1.py failed')
    exit()


# print ('Execution Time: ', time.time()- start ,' Seconds')
print(orders_df.groupby('Sales'))

# trends_df = orders_df.groupby('Sales').filter(lambda x: sum(x['var']) > 2000000)
trends_df = orders_df.groupby('Sales').filter(lambda x: sum(x['var']) > 2000000)

# Group by animal category
trends_df = orders_df.groupby("Sales")
# Apply mean function to wieght column
# animal_groups['weight'].mean()
print(trends_df)
