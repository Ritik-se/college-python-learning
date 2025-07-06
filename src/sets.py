# #sets are built in data type that is used for collecting unique elements 
# #they donnot aloow duplicate element.   
# # its is used for mathematical operation 
# #creating a sets
# myset={1,2,34,5}
# print(type(myset),myset)
# #empty set
# my=set()
# print(type(my))
# #addinf list or tuple in it 
# my=set([1,2,3,45])
# print(type(my))
# print(my)
# #unique set they ingnore the repeting elemnt and cosiderd only first written element
# my=set([1,2,35,5,6,7,5,5,5,])
# print(type(my))
# print(my)
# #basic set operation 
# #add,remove
# my_set={1,2,4,5,5,}
# my_set.add(8)
# my_set.add(8)#ignore this duplicate item 
# my_set.remove(2)#it gives error if element is not present 
# my_set.discard(11)# it not shoes erroe even it is not present
# print(my_set)
###pop
elel=my_set.pop()#it remove and return first inserted element 
##clear
my_set.clear()
#set membership test
my_set={1,2,34,5}
print(3 in my_set) # it evalude our set and give rather the element 
#is present or not if not they gave false if present they gave true 
print(10 in my_set)
#mahematical opration
set1={1,2,34,5,5,6}
set2={1,2,34,5,5,6}
#union



