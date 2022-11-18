for i in range(1,6):
    x=""
    for j in range(1,i+1):
        x=x+" "
        if(j%2==0):
            x=x+str("0")
        else:
            x=x+str("1")
    print(x)

