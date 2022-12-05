def add(n1,n2):
    return n1+n2
def mul(n1,n2):
    return n1*n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2


opreasiton={
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

num1=float(input("first number:"))
for symbol in opreasiton:
    print(symbol)
opreasiton_symbol=input("pick a opreastion")
num2=float(input("second number:"))

clalculator_functon=opreasiton[opreasiton_symbol]

ans=clalculator_functon(num1,num2)

print(f"{num1} {opreasiton_symbol} {num2} = {ans}")