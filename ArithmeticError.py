"""
@author VRAJ PATEL (20CE111)

"""
try:
    a = 10/0
    print (a)
except ArithmeticError:
        print ("This statement is raising an arithmetic exception.")
else:
    print ("Success.")
