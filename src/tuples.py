# #introduction to tuples
# # list is converted in to tuple and tuple also c
 # onverted into
# # tuple are same as list but it is immutable
# #creating a tuple ()    
# tup=()
# print(tup,type(tup))
# # create empty tuple
# tup=tuple()
# #add element
# tup=tuple([1,2,3,4,5,6,])
# print(tup,type(tup))
# #mixed
# tup1=(1,2,3,"ritik","chintu")
# #accessing tuple element 
# print(tup1[0])
# print(tup1[-1])
# #accessing and slicing operation is similar as an list 
# #tuple operation 
# concatenation=tup1+tup
# print(concatenation)
# #tuple times operation
# print(concatenation*3)
# #IMMUTABLEE NATURE OF TUPLES
# #elements not changed once assign   
# names=("ritik","rohant","shubh")
# # names[1]="krish"
# # print(names)
# #tuple meathods
# print(names.count("ritik"))
# print(names.index("ritik"))
# #packing and unpacking tuple
# #whenever we gave data with coma sep 
# #it return and packed it in tuple
# packed_tup=1,2,3,"ritik","manoj"
# print(packed_tup)
# #unpacking with known vairable
# a,b,c,d,e=packed_tup
# print(a)
# print(b)
# print(c)
# #unpack using * it do till we start to the end
# first,second,*middle,last=packed_tup
# print(first)
# print(second)
# print(middle)
# print(last)
# #nested tuple we have list inside the tuple
lst=([1,2,3,4],(1,2,3,4,),(3,"ritik"))
# print(lst[0][2])
# print(lst[0][0:3])
# #iterating over nested tuple
for sub in lst:
    for i in sub:
        print(i,end=' ')
    print()

    



