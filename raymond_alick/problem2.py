try:
    from problem1 import data_df as data_df
except ImportError:
    print ('Error! Importing problem1.py failed')
    exit()


# print ('Execution Time: ', time.time()- start ,' Seconds')
print(data_df)