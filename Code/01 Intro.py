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

x=5
name="Raj"
print(x)
print(name)
#=====================================================

age=21
_color="Green"
total_score=90

print()

# =========================================

a=b=c=100  # assign same value
print(a)
print(b)
print(c)

# ========================================================

a,b,c=100,200,300  # assign different value
print(a)
print(b)
print(c)


# =============================================

x="Rajveer"
print(id(x))
y=x
print(id(y))

# =================================================

x="Rajveer"
print(x)
del x  # delete x
print(x)

# ==============================================

a,b=10,200
print(a,b)
b,a=a,b
print(a,b)

# ==================================================

s="Rajveer Singh"
print(len(s))

# Arithmetic operator ==================================================

a=15
b=4

print("addition", a+b)

print("subtraction ", a-b)

print("Multiplication ", a*b)

print("Division ",a/b)

print("Floor division ", a//b)

print("modulus ",a%b)

print("exp ", a**b)

# Comparison operator ============================================================================

a=15
b=4

print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

# logical vs binary ??

# Logical operator ====================================================================


# Assignment operator ==========================================================

a=10
b=20
z=0

print(a)
print(b)

z+=1
print(z)

z*=2
print(z)

z-=1
print(z)

# Identity operator ==========================================================

a=10
b=10

print(a is b)

print(a is not b)

# membership operator ==========================================================

l=[10,34,56,889,55,332,11,223]
a=111

print(a in l)

print(a not in l)

# ternary  operator ==========================================================

a,b=100,200

min = a if a<b else b
print(min)

max = a if a>b else b
print(max)

# =====================================================================================

name=input("Enter name : ")
if name =="rajveer":
    print("Hello  Rajveer")
print("Hello there ")

# ====================================================================================

name = input("Enter name : ")
if name == "rajveer":
    print("hello rajveer")
else:
    print("Hello guest")

# =====================================================================================

brand = input("enter brand ...")
if brand =="RC":
    print("its children's brand")
elif brand =="KF":
    print("its KF brand")
elif brand =="FO":
    print("Its FO brand")
else:
    print("Unknown brand")

# ========================================================================================

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
if num1 > num2:
    print("Biggest number is ", num1)
else:
    print("Biggest number is ",num2)

# ===================================================================================

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
num3 = int(input("Enter third number "))

if num1>num2 and num1 >num3:
    print("Biggest number is ", num1)
elif num2>num3:
    print("Biggest number is ", num2)
else:
    print("Bigegst number is ",num3)\


# ===============================================================================

num = int(input("Enter number : "))
if num>=1 and num<=10:
    print("Number ", num, "is between 1 and 10")
else:
    print("Number ", num,"is not between 1 and 10")

# LOOP ===========================================================================
s="Rajveer Singh"
for i in s:
    print(i,end=" ")

s="Rajveer Singh"
i=0
for x in s:
    print("char present at index ",i,"is ",x)
    i+=1

# Range ====================================================================================

for i in range(10):
    print("Hello")

for i in range(10):
    print(i)

for x in range(1,21):
    if x%2==0:
        print(x, end=" ")

for x in range(1,21,2):
    print(x)


# =====================================================================

list = eval(input("enter list"))
sum=0
for x in list:
    sum = sum+x

print(sum)

x=1
while x<=10:
    print("Loop")
    x=x+1


num=int(input("Enter number "))
sum=0
i=1
while i<=num:
    sum=sum+i
    i=i+1
print(sum)

name = input("enter name ")
while name!="Raj":
    name = input("enter name ")

print("Thanks")


for i in range(5):
    for j in range(5):
        print("i --> ", i," "," j --> ",j)


# ==========================================================================================

age = int(input("Enter age "))
if age >18:
    print("Eligible")
else:
    print("not eligible ")


age = int(input("Enter age "))
if age >18:print("Eligible")
else:print("not eligible ")


marks = int(input("Enter marks"))
result = "Pass" if marks>33 else "Fail"
print(result)


age = int(input("enter age "))
if age <=12:
    print("child")
elif age >12 and age <20:
    print("Teenager")
else:
    print("adult")


age = int(input("enter age "))
if age <=12:
    print("child")
elif 12 < age < 20:
    print("Teenager")
else:
    print()


age = int(input("enter age "))
is_member = True

if age > 60:
    if is_member:
        print("30% discount")
    else:
        print("20% discount")

else:
    print("Not eligible for adult discount")

age =30
s = "adult" if age >18 else "Minor"
print(s)


# Match

number = 30
match number:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("Three")
    case _:  # default case
        print("Invalid")


number = 3
match number:
    case 1|2|3:
        print("one/two/three")
    case 4|5|6:
        print("four/five/six")
    case 7|8|9:
        print("seven/eight/nine")
    case _:  # default case
        print("Invalid")

def friends_in_trouble(j_angry, s_angry):
    if j_angry == True and s_angry == True:
        return "Since both of them are angry, you are in trouble"
    elif j_angry == True or s_angry == True:
        return "Only one of them is angry, you are not in trouble"
    else:
        return "Neither of them is angry, you are not in trouble"

print(friends_in_trouble(True, True))


def friends_in_trouble(j_angry, s_angry):
    if j_angry == True and s_angry == True:
        return True
    elif j_angry == True or s_angry == True:
        return False
    else:
        return False

print(friends_in_trouble(False, True))

def checkOddEven(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(checkOddEven(6))

num = int(input("Enter number "))
if num <= 100:
    print("num")
else:
    print("Big")











