for i in range(1,6):
    x = ""
    for j in  range(1,6):
        if i<=j:
            x=x+str(j)
        else:   
             x=x+" "    
    print(x)