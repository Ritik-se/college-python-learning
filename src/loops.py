#loops for while nested loops 
# control statement contine break
#range(5) it i basically 0-5 {0 to n-1}
for i in range(5):
    print(i)    #last no is included
for i in range(0,6): #iterate over 0 to 6
    print(i) 
for i in range(1,10,1): # it shows that it start with 1 iterate over 10 and increase by 1 
    print(i) 
for i in range(1,10,2): # increase by 2
    print(i)    
for i in range(10,-1,-1): # decrease by 1
    print(i)    
#string in string we can traverse over each and every charachter    
str="krish naik"
for i in str:
    print(i)

#while loop it countinue untill and unless conditon is true     
count=0
while(count<5):# it iterate over 0 to 5-1=4
    print(count)
    count=count+1 # inc and dec

#loop control statements 
##break it exits the loop prematurely
for i in range(0,10):
    if(i>=8):
        break # it break the loop   
    print(i)

#continue statement 
# it skips current iteration and countine with next 
for i in range(10):
    if(i%2==0):
        continue
    print(i)
         
#pass statement is null operation it do nothing 
for i in range(5):
    if(i==3):
        pass # it does nothing like a uno pass
    print(i)

#nested loops it is a loop inside the loop 
for i in range(0,3,2):
    for j in range(i):
        print("inner loop executed")
    print(i,"value of i")

# sum of natural no 
n=int(input("enter the no"))
sum=0
#while(count<=n):
#     sum=sum+count
#     count=count+1
# print(f"sum of {n} natural no is",sum)
for i in range(n,0,-1):
    sum=sum+i
print(f"sum of {n} natural no is ",sum)

#prime no 
num=int(input("enter the prime no"))
count=0
if(num==0 and num==1):
    print("not a prime not a composite")
else:
    for i in range(1,num+1,1):
        if(num%i==0):
            count=count+1
if(count==2):
    print(f"{num} is prime no")
else:
    print(f"{num} is not a prime")

# prime no in a range 0,100
nu=int(input("enter the maximum no you want to find all prime"))
for num in range(1,nu+1,1):
    if(num>1):
        for i in range(2,num,1):
            if(num%i==0):
                break
        else:
             print(num)

     





    