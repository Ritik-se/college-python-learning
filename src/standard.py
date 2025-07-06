# # #standard library in python is a collection of an module and packages that come bundle with python 
# # #providing vide range of functionality 
# # #array is imp library wich is used to create an array 
# # # i shows what type of data store i means int f means float so 
# # #they can allocate some memory
# # import array
# # arr=array.array('i',[1,2,3,4,56])
# # #random
# # import random
# # #randint helps to give us one random integer from the range 
# # print(random.randint(1,100))  
# # #choice in random is used to choice in multiple choice
# # #in case of collection
# # print(random.choice(["apple","mango","papaya"])) 
# # ## os is used for file and directory access
# # import os
# # #get current directory
# # print(os.getcwd())
# # #make directory
# # os.mkdir("bhenjo")
# # ##high level operation on filr or collrction of file
# # import shutil
# # # copy the data of one file to the another          
# # shutil.copyfile('srcc.txt',"dest.txt")
# # # data serialization 
# # #used for efficient storage 
# import json
# # if we wanna convert data dat we use dump
# data=[1,2,34,5,6,]
# json_str=json.dumps(data)
# print(json_str)
# print(type(json_str))
# # to convert it back 
# pastdata=json.loads(json_str)
# print(pastdata)
# print(type(pastdata))
# #csv use to work with csv file
# import csv
# # we use open func to open it by using file name and mode
# with open("example.csv",mode='w',newline='')as file:
#     writer=csv.writer(file)
#     writer.writerow(["name","age"])
#     writer.writerow(["krish","14"])
#     with open("example.csv",mode='r') as file:
#  reader=csv.reader(file)
#  for row in reader:
#     print(row)

##date time 
from datetime import datetime,timedelta
now=datetime.now()
print(now)
print(now-timedelta(days=1))
##time
import time
##sleep the program 
print(time.time())
time.sleep(2)
print(time.time())
##regular expression basicaaly helps to match 
import re
pattern=r'\d+'
text='there are 123 apples'
match=re.search(pattern,text)
print(match.group())


    




