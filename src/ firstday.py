#case sensitive
name='ritik'
Name='chintu'
print(name)
print(Name)
#indentation
age=10
if age>30:
    print(30)

print ("hello")#it prints every time it come out of the loop

#line continuation
#we use backslash to continue command in another line 
total=1+2+3+\
4+5+7
print(total)

#multiple statement in a single line (we use ; to do multiple statement in a single line )
x=0;y=10;z=x+y
print(z)
#sementics in python
#type function is used to find data type of the variable 
#typeinfrence variable type detemine at run time 
variable=10
print(type(variable))
variable='ritik'
print(type(variable))
# #name error
# a=b;bis not defined
#code example of indentation 
if True:
    print("inside the if ")
    if False:
        print("insie the false")

print("imalwaysprinteed")

#variable 
a=100       #
#declaring and asiigning variable  declaration of variable is done by asigning values variable 
age=32
height=6.1
his=True
#print variable 
print("age",age)

#python is dynamicaly typed type of variable is determined during the run time only

#naming convential
#variabale name is case sensitive
#its name should be discriptive
#not start with a letter 2name= not 
# not use @ and operator btw the variable 
#   type checking and conversion 
#type casting
print(age)
string=str(age)
print(type(string))
age=int(string)
print(type(age))

# name="krish"
# int(name)#not posiible to convert the sting into int 
height=5.8
print(int(height))

#python allow to change the type as an code executees
##dynamic typing
var=10
print(var)
print(type(var))

var="ritik"
print(var,type(var))

var=3.24
print(var,type(var))

#input
#input function allways return a string type 

age=input("enter the age")
print(age,type(age))
age=int(input("enter the age"))
print(age,type(age))

## calcualator
a=float(input("enter the first no"))
b=float(input("enter the second no"))
print("the sun of a and b is:",a+b)
print("the sub of a and b is:",a-b)
print("the mult of a and b is:",a*b)
print("the  div of a and b is:",a/b)
# data types
#integers
age=35
type(age)
#floating ponit
flt=38.0098
print(flt,type(flt))
#string
str="ritik"
print(str,type(str))
#boolean
True
print(type(True))
dec=True
print(dec,type(dec))    
a=10
b=20
type(a==b)

#common errors
#result="ritik"+5 # we cannot concatenate int with string we need to type casting
result="ritik"+str(5)#we covnvert int into string an conatenate it    
print(result,type(result))
ans="ritik"+"agrawal"
print(ans,type(ans))
# operator
#airthamtic operation 
a=20
b=15
res=a+b #-/%
print(res)
# floor division (//) it removes the decimal and give us output
res2=a//b
#exponential(**)    
res3=a**b #a^b
#comparison operator
#== they compare that a is equal or not they are case sensitive retun t or f
#!= not equal to  return true or flase
#><grator than less than  return true or flase

a=10
b=20
print(a==b)
str1="krish"
str2= "krish"
print(str1==str2)

###logical operator
##And both the param should be true 
x=True;y=False
print(x and y)
#or one of both the parameter is true then it give us true
f=False
t=True
print(f or t)
# not inverse of any boolean variable
print(not t)
#swapping is done in python by a,b=b,a
#we can print element in double quotes by { } this brackets 
''' f"" is a formatted string literal
Adding f before the string lets you insert variables or expressions directly inside {}.'''

#string is acess by string name and indexing we. can also do string[1:5] to scess string from 
1 to 5-1=4

