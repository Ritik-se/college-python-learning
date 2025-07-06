#list is oderd mutable collection of item mutable means we can change it 
# it also contain a data of diff data types index 0-n
#define
lst=[]
print(type(lst))
names=["ritik","manoj","krish",1,2,3,4,5]
print(names)
mixedlist=[1,2.3,"ritik"]
print(mixedlist)
#accessing the element in list  
print(names[0])
print(names[7])
print(names[-1]) # -ve indexing 
print(names[-2])
print(names[-8])
print(names[0:8])#range printing 
print(names[1:8])
print(names[0:7])
print(names[:8])# if there is blank space we get an there list length or 0
print(names[0:])
## modify list element 
names[1]="mohan"
print(names)    #it takes from index and do word seap charchter   
#[f', 'i', 's', 'h', 'i', 'i', 'i', 'i', 'i', 'i']   
names[0:]="fishiiiiii"
print(names)
## LIST MEAATHODS
#append is used to add element inside the list
names.append("chintu")
#insert function is used to insert value at specific index
names.insert(1,"rohit")
print(names) 
names=["ritik",'chintu','sweetu','chintu']
#its used to remove names in list 
#remove first occurence 
names.remove("chintu")
names.remove("chintu")
print(names)
# remove and return last item 
tt=names.pop() # it return the last element.        
print(tt)
print(names)
names=["ritik",'chintu','sweetu','chintu']
#find index it return index
index=names.index("sweetu")
print(index)
names.insert(2,'banana')
print(names)
#count shows no of times the element occures
print(names.count("chintu"))
#sort in ascending order
sort=names.sort()
print(sort)
# reverse the list 
names.reverse()
# clear all elements of the list 
names.clear()

## list sclicing 0----n-1
num=[1,2,3,4,5,6,7,8,9,10]
print(num[:5])
print(num[5:])
print(num[:])
print(num[::2])
print(num[::-1])
print(num[3:5])
#iterating over list 
for name in num:
    print(name)
#iterate over index we use enumerate fun
for index,name in enumerate(sum):
    print(index,name)
    # for range
for name in range(3,5):
    print(num[name])

## list comprehension
lst=[]
for i in range(0,10):
    lst.append(i**2)
print(lst)

#or ope.    iteration
lst=[x**2 for x in range(0,10)]
print(lst)
#[ printwantexpression for item in range]
#[expression for item in range if conditon]
lst=[num for num in range(0,11) if(num%2==0)]
print(lst)
#nested list compherension 
#[ printwantexpression for item1 in range1 for item2 in range2]
lst1=[1,2,3,4,5]
lst2=['r','v','c']
pair=[(lst1[i],lst2[j]) for i in range(0,5) for j in range(0,2)] 
print(pair)

## 
from turtle import clone


words=["riiti","chintu","rohant"]
lenth=[len(i) for i in words]
print(lenth)
       
#use of else block in list comprehension 
# if clone goes after the for.

# if...else must go before the for.

lst=[ 1 if(lenth[x]%2==0)else 0 for x in range(3)]
print(lst)
# it is used to create a empt list 
lst=lst((1,2,3,4,5,6))
print(lst)
#nested list inside th elist we also have tuples
lst=[[1,2,3,4],[1,2,3,4,],(3,"ritik")]
print(lst[0][2])
print(lst[0][0:3])
    
