# a=10
# b=20
# print(f"{a} == {b}: {a == b}")
# #conditonal statements 
# #if statements evalute condition and execute a block 
age=20
if(age>=20):
    print(age,"allow to vote.")
#else if block is false
else:
    print("u are a minor ")
#elif allows to check multiple condiitn
age=9
if(age>18):
    print("u are adult")
elif( age>7 and age<=18):
    print("you are at adolesens ")
else:
    print("ure a child")

    #nested conditional statements 
# we can put if elif else statemeent inside id elif else statemennt
num=30
if(num>0):
    print("no is positive")
    if(num%2==0):
        print("no is even")
    else:
     print("no is odd")
else:
    print("no is negative")

#usecasee
#determine year is a leap year
num=int(input("enter the year"))
if num%4==0:
    if(num%100==0):
        if(num%400==0):
            print("year is leap year")
        else:
            print("leap not  year")
    else:
        print("leap year")
else:
    print("no is not a leap year")

#calculater seitchcase in if and else

num1=int(input("enter the no 1 "))
num2=int(input("enter the no 2 "))
ope=str(input("enter the opearation +,-,*,/,//,%,^ : "))
if(ope=='+'):
    print("adiition is",num1+num2)
elif(ope=='-'):
    print("subtraction is ",num1-num2)
elif(ope=='*'):
    print("multiplication is ",num1*num2)
elif(ope=='/'):
    if(num2!=0):
     print("division is ",num1/num2)
    else:
        print('error num2 is zero')
elif(ope=='%'):
    print("modulus is ",num1-num2)
elif(ope=='//'):
    if(num2!=0):
     print(" floor division is ",num1//num2)
    else:
        print('error num2 is zero')
elif(ope=='^'):
    print("modulus is ",num1**num2)
else:
    print("invalid operation")
