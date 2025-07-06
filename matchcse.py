x=int(input("enter the no"))
match x:
    case 2:
        print("smaller")
    case 5:
        print("bigger")
    case _ if(50>x):
        print("not valid input")
    case _ if(50<x):
        print("large input")

        
 

    