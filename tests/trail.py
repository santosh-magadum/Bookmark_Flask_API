

# print("Hi")
# import numpy as np
# import pandas as pd 
# emp_name=['a','b','c']
# emp_id=[1,2,3]

# df=pd.DataFrame([[data1,data2] for data1,data2 in zip(emp_name,emp_id)],columns=['Employee Name','Employee Id'])


# df=pd.DataFrame(zip(list(emp_name),list(emp_id)),columns=['Employee Name','Employee Id'])

# df["salary"]=[10000,20000,np.nan]

# df['salary']

# na_data=df.isna().sum()
# print(na_data.index)

# for col_name,count in zip(list(na_data.index),na_data):
#     if count>0:
#         df[col_name]=df[col_name].fillna(np.mean(df[col_name]))

# print(df)

arr=[1,2,3,5,7,9,12]

count=0

def func_(t_arr,output):
    t_count=0
    for index_1 in range(len(t_arr)-1):
        for index_2 in range(index_1+1,len(t_arr)):
            # print(t_arr[index_1],t_arr[index_2])
            if t_arr[index_1]+t_arr[index_2]==output:
                t_count+=1
    return t_count                

# func_([1,2,3],5)
for index in range(2,len(arr)):
    count+=func_(arr[:index],arr[index])

print(count)




