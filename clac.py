# def calc(x,y,o):
#     if o=='a':
#         return x+y
#     elif o=='s':
#         return x-y
#     else:
#         return x*y
# if __name__=='__main__':
#     print(calc(10,20,'a'))
#     print(calc(10, 20, 's'))
#
# 1. write a program to collect the customer name and write it into a file called
# customer.txt until we get bye form user
#
# argparse ->argument parser
# sys.argv
import sys
with open('customer.txt','a') as fo:
    while True:
        name=input("Enter your name:")
        if name == 'bye':
            print("Thank you!")
            sys.exit()
        fo.write(name+"\n")
