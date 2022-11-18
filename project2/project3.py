def addition(a,b):
    z=a+b
    return z

def multiply(a,b):
    z=a*b
    return z

def division(a,b):
    z=a/b
    return z

def subtraction(a,b):
    z=a-b
    return z

def start_cal():
    try:
        x=float(input("enter number :"))
        y=float(input("enter number :"))
    except ValueError:
        print("valeu is not number")
    try:
        action=input("enter action :") 
        assert action == "+" or action=="-" or action=="*" or action=="/","not valid" 

    except AssertionError:
        print("not valid.......")

    if action == "+":
        print(addition(x,y))
    elif action == "*":
        print(multiply(x,y))
    elif action == "/":
        print(division(x,y))
    elif action == "-":
        print(subtraction(x,y)) 
            

start_cal()
