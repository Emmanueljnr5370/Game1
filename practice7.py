#import math
#from math import factorial

#n = (4,6,7,14)
#for x in n:
#    print(factorial(x))















#import math
#from math import factorial

#x = int(input('Enter any number>> '))
#print(factorial(x))


#list1 = list(range(1,11,3))
#print(list1)




#x = 11
#lst = list(range(0,x))
#for n in lst:
#    print(n)

#  Program to display the Fibonacci sequence up to n-th term

nterms = int(input('How many terms>>? '))

# For the first two terms
n1, n2 = 0, 1
count = 0

# Checking if the number of terms is valid
if nterms <= 0:
    print('Please enter a positive integer')
# But if there's only one term, return n1

elif nterms == 1:
    print('Fibonacci sequence: upto', nterms, ':')
    print(n1)
# Generating Fibonaci sequence    

else:
    print('Fibonacci sequence>> ')
    while count < nterms:
        print(n1)
        nth = n1 + n2
       # Update values
        n1 = n2 
        n2  = nth
        count += 1
        





























