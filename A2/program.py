#
# Write the implementation for A2 in this file
#

# UI section
# (write all functions that have input or print statements here).
# Ideally, this section should not contain any calculations relevant to program functionalities

import math
"""
def print_menu_options():
    print("1 - Read\n"
          "2 - Print\n"
          "3- SameModulus\n"
          "4-IncreasingModulus"
          "x - exit")

def run_menu():
    list = []
    options = {1: Read, 2: Print, 3: SameModulus, 4:IncreasingModulus}
    while True:
        print_menu_options()
        opt = input("option=")
        if opt == "x":
            break
        opt = int(opt)
        options[opt](list)
        Secv=[]
        if opt == 1:
            list=Read()
        if opt == 2:
            Print(list)
        if opt == 3:
            SameModulus(list,LimR,LimL)
            Print(Secv)
        if opt==4:
            IncreasingModulus(list,LimR,LimL)
            Print(Secv)
run_menu()
    """

def Read():

    """
    Reads a list of complex numbers. On the even position are the real parts and on the odd positions are the imaginary parts
    After every complex number read there it is printed the list
    It returns the list
    """

    l=[]
    x=input("Give the real part:")
    y=input("Give the imaginary part:")
    while (x!=""):                     #terminare cu ENTER
        x= int(x)
        y=int(y)
        l     = l+[x]
        l=l+[y]
        print (l)
        x=input("Give the real part:")
        y=input("Give the imaginary part:")

    return l

def Print(list):
    for i in list:
        print(list[i]," ",list[i+1],"i")
        print('\n')


# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

# print('Hello A2'!) -> prints aren't allowed here!


    """
    The function receives 2 parameters, real numbers and returns the modulus of the complex number created by them 
    a,b are the real part respecrtively the imaginary part
    a,b are real numbers '
    it returns the value of the modulus
    """
def Modulus(a,b):
    a=a*a
    b=b*b
    m=a+b
    m=math.sqrt(m)
    return m

def Long(list,i):
    j=i
    a=list[j]
    b=list[j+1]
    while(j<=len(list) & Modulus(a,b)==Modulus(list[j+2],list[j+3])):
          j=j+2
          a=i
          b=a+1
    return j-2

def SameModulus(list, limR, limL):
    i=1
    a=i
    b=a+1
    while (i<=len(list)):
        mod1=Modulus(a,b)
        i=i+2
        a=i
        b=a+1
        mod2=Modulus(a,b)
        while (i<=len(list)& mod1==mod2):
            i=i+2
            a=i
            b=a+1
        j=Long(list,i)
        m=j-i
        p=LimR-LimL
        if(m>p):
            LimL=i
            LimR=j
        i=j+2

def Long1(list,i):
    j=i
    a=list[j]
    b=list[j+1]
    while(j<=len(list) & Modulus(a,b)<=Modulus(list[j+2],list[j+3])):
          j=j+2
          a=i
          b=a+1
    return j-2

def IncreasingModulus(list, limR, limL):
    i=1
    a=i
    b=a+1
    while (i<=len(list)):
        mod1=Modulus(a,b)
        i=i+2
        a=i
        b=a+1
        mod2=Modulus(a,b)
        while (i<=len(list)& mod1<=mod2):
            i=i+2
            a=i
            b=a+1
        j=Long1(list,i)
        m=j-i
        p=LimR-LimL
        if(m>p):
            LimL=i
            LimR=j
        i=j+2

def print_menu_options():
    print("1 - Read\n"
          "2 - Print\n"
          "3- SameModulus\n"
          "4-IncreasingModulus"
          "x - exit")

def run_menu():
    lista = []
    options = {1: Read, 2: Print, 3: SameModulus, 4:IncreasingModulus}
    while True:
        print_menu_options()
        opt = input("option=")
        if opt == "x":
            break
        opt = int(opt)
        options[opt](lista)
        Secv=[]
        if opt == 1:
            lista=Read()
        if opt == 2:
            Print(lista)
        if opt == 3:
            LimL=0
            LimR=0
            SameModulus(lista,LimR,LimL)
            Print(Secv)
        if opt==4:
            LimL=0
            LimR=0
            IncreasingModulus(lista,LimR,LimL)
            Print(Secv)
run_menu()