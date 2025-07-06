#import module in python
#open source proh language  
#it helps to organize and reuse the code
# import package 
import math
print(math.sqrt(6))
#import the package and directly use it 
from math import sqrt,pi
print(sqrt(16))
print(pi)
#every package has a multiple function wich we can directly use it 
#nupy library is used to perform operation on array or a diff operation of array 
import numpy as np #np is alies it use as a placeof numpy 
np.array([1,2,4,5])
from math import * # import eveey module 
print(sqrt(16))
#define my own costume module i should be able to any other code    
from package.add import *
#calling packages
print(addition(2,5))
from package import *
add.addition(4,5)
##calling subpack 
from package.subpackages import subpack
print(subpack.multiply(5,3))