print("Hello world")

# ============================================================

a=10
b=20
print(a+b)

# keywords =======================================================

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

import keyword
print(dir(keyword))  # print all functions present in the keyword

# id and type  ====================================================================================

a=10
b=20
print("Id of a - ",id(a))
print("Id of b - ",id(b))

print("type of a - ", type(a))
print("type of b - ", type(b))

# Binary conversions ==================================================================================
a=10
b=20

print("Original number ", a)
print("Original number ", b)

print("After binary conversion ")

print(bin(a))
print(bin(b))

# Octal conversion =================================================================================

a=10
b=20

print("Original number ", a)
print("Original number ", b)

print("After octal conversion conversion ")

print(oct(a))
print(oct(b))

# Hexa decimal converson =============================================================

a=10
b=20

print("Original number ", a)
print("Original number ", b)

print("After binary conversion ")

print(hex(a))
print(hex(b))

# hexa to decimal ============================================================

a=10
b=20

print("Original number ", a)
print("Original number ", b)

print("After binary conversion ")

z = hex(a)
print("Hexa ", z)

print("Convert hexa to decimal")

print(int(z,16)) # base 16

# Type casting ================================================================================

a=10
b=20.33

print("value of a ",a)
print("value of b ",b)

print("Type casting")

print(float(a))
print(int(b))
print(bool(a))
print(str(b))
print(complex(b))

# input =============================================================================

name=input("enter your name : ")
print("my name is ",name)

name,email=input("enter your name : ").split()  # by default split is space
print("my name is ",name, " my email is ",email)


name,email,phone=input("enter your name : ").split()  # by default split is space
print("my name is ",name, " my email is ",email, " my phone no is ",phone)

name,email,phone=input("enter your name : ").split(",")  # split using comma
print("my name is ",name, " my email is ",email, " my phone no is ",phone)


value=int(input("enter value : "))
print("value is ",value)

# ========================================================================================

a="Rajveer"
b=100
c=23.44
d=("Rajveer","Singh","Indore")
e=["Rajveer","Singh","Indore"]
f={"Rajveer","Singh","Indore"}
g=set(e)
h={1:"Rajveer",2:"Singh",3:"Indore"}

print(type(a))  # string
print(type(b))  # int
print(type(c))  # float
print(type(d))  # tuple
print(type(e))  # list
print(type(f))  # set
print(type(g))  #set
print(type(h))  #dict

# ==================================================================================

my_list=[10,33,55,778,9,33, 20.22,True]
print("My list ",my_list)
print("Convert list to set")
my_set=set(my_list)
print("My set ", my_set)


# =====================================================================================




