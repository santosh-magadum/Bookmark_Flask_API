

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

# arr=[1,2,3,5,7,9,12]

# count=0

# def func_(t_arr,output):
#     t_count=0
#     for index_1 in range(len(t_arr)-1):
#         for index_2 in range(index_1+1,len(t_arr)):
#             # print(t_arr[index_1],t_arr[index_2])
#             if t_arr[index_1]+t_arr[index_2]==output:
#                 t_count+=1
#     return t_count                

# # func_([1,2,3],5)
# for index in range(2,len(arr)):
#     count+=func_(arr[:index],arr[index])

# print(count)


# (select * from employee_table groupby Depart  )   
# order by salary desc limit 3




dict_={'a':1,'b':2,'c':{'f':4,}}

# dict_['a']
# dict_.get('a')
x='abcdef'
# print(x[::-1])

# len()
# list_.sort()
# sort()


# [ for]
# class Employee: 
#     val=10 
#     def __init__(self): 
#         print('Employee created') 
#     def __del__(self): 
#         print("Destructor called") 
#         del val 
         
# def Create_obj(): 
#     print('Making Object...') 
#     obj = Employee() 
#     print('function end...',obj.val) 
#     return obj 
# print('Calling Create_obj() function...') 
# obj = Create_obj() 
# print('Program End...')
# print(Employee.val)



# 1. Create a class named InfiniteInterviewQuestions
#    1. Define a method to ReadInputDataSet set
#    2. Define a method to process the data and provide the solution. Call the method, GetSolution


# 2. Inherit from it another class named EvenSquaresFiltering, Inside this class
#    1. Implement ReadInputDataSet() to read the list of inputs provided by the interviewer.
#    2. Create a constructor method that accepts a list of numbers and can invoke ReadInputDataSet
#    3. Implement the method GetSolution to,
#       1.  Use a hashmap based data structure to  store keys as the input data values from ReadInputDataSet and set their values to 1
#       2. Update the hashmap in step 1 to append values to square of the key. For instance,
#          1. If the key is 1, the value is updated to 1*1 = 1
#          2. If the key is 2, the value is updated to 2*2 = 4
#       3. Create a method RemoveOddValues  to Update the hashmap to remove all the keys where the value is no an even number. For instance, 
#          1. If the key is 1, the value is 1*1 = 1, which is odd, the hashmap should be updated to remove these values. 
#    4. Create a method in the object to show first 50 elements in the hashmap in ascending order by key. MethodName: First50ByKey
#    5. Create a method in the object to show last 50 elements in the hashmap in descending order by key MethodName: Last50ByKey
# 3. Construct an object using this class with a list of numbers provided/instructed by the interviewer, and
#    1. Call GetSolution
#    2. Call First50ByKey
#    3. Call Last50ByKey

 

# Caveats to look for:

 

# 1. The input may not always be correct while construction is being done for the object
# 2. If the list/criteria provided as input is NOT containing all the integers only, then the solution is expected to construct the hashmap for values that are integers and drop other values. The dropped values should be printed on screen.



# class InfiniteInterviewQuestions():
	
	
# 	def ReadInputDataSet(input_):
# 		return input_


# 	def GetSolution():
# 		pass

# 	def RemoveOddValues():
# 		pass


# class EvenSquaresFiltering(InfiniteInterviewQuestions):
	

# 	def __init__(self,list_of_numbers):
# 		self.list_of_numbers=list_of_numbers
# 		self.read_input_dataset=self.ReadInputDataSet(list_of_numbers)
# 		dict_={}

# 	def GetSolution(self):
# 		for data in self.read_input_dataset
# 			dict_[data]=1
# 			dict_[data]=data*data

# 	def RemoveOddValues(self):
# 		for key,value in dict_.items():
# 			if value%2!=0:
# 			dict_.remove(key)

# def First50ByKey(obj):
# 	data=obj.dict_
 
# 	sorted(data.items() , key=lambda d:d[1])



class ArrayList:
   def __init__(self, number_list):
       self.numbers = number_list
   def __iter__(self):
       self.pos = 0
       return self
   def __next__(self):
       if(self.pos < len(self.numbers)):
           self.pos += 1
           yield self.numbers[self.pos - 1]
       else:
           raise StopIteration
array_obj = ArrayList([1, 2, 3])
it = array_obj
print(next(it)) #output: 2
print(next(it)) #output: 3
print(next(it))






# func_=lambda p,t,r:(p*t*r)/100

# # print(func_(100,2,8))

# rate_int=lambda p,t,i:(i)/(p*t)



# def rate_of_interest(**kwargs):
#     # print
#     mul=1
#     for e in kwargs.values():
#         if e==0:
#             continue
#         mul*=e
#     add=sum(kwargs.values())

#     return add/mul

# data={'inflation':1,'repo_rate':1,'npa':1,'bank_rating':1 }



# interest=rate_of_interest(**data)
# # print(interest)

# # output=rate_int(100,2,interest)
# # print(output)




# final_out=func_(100,2,interest)
# print(final_out)


# import pandas as pd
# from io import BytesIO 

# df = pd.read_csv(BytesIO("C:/Users/PC/Documents/wiki.txt"))




# data=pd.read_csv("C:/Users/PC/Documents/wiki.txt",encoding='latin1')
# print(data)

# print(df)

entire_word=[]
with open("C:/Users/PC/Documents/wiki_para.txt") as data:
    list_data=data.readlines()
    for each_line in list_data:
        each_char_list=each_line.split(" ")
        entire_word=entire_word+each_char_list

print(entire_word)





