def add(x,y):return x+y 
def subtract(x,y):return x-y 
def multiply(x,y):return x*y 
def divide(x,y):return x/y 
print("select operation:+,-,*,/")
op=input("enter operator:")
a=float(input("enter first number:"))
b=float(input("enter second number:"))
if op=='+':print("result:",add(a,b))
elif op=='-':print("result:",subtract(a-b))
elif op=='*':print("result:",multiply(a*b))
elif op=='/':print("result:",divide(a/b))
else:print("invalid operator")