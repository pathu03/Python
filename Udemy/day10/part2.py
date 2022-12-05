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
def calculetor():
    num1=int(input("first number:"))
    for symbol in opreasiton:
        print(symbol)

    shoud_continua=True
    while shoud_continua:
        opreasiton_symbol=input("pick a opreastion")
        num2=int(input("next number:"))

        clalculator_functon=opreasiton[opreasiton_symbol]

        ans=clalculator_functon(num1,num2)

        print(f"{num1} {opreasiton_symbol} {num2} = {ans}")
        if input(f"type 'y' of continue with{ans}, or type 'n' for star new calculator:"):
            num1=ans
        else:
            shoud_continua=False
            calculetor()
calculetor()