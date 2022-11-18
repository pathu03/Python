for i in range(1,6):
    count = 1
    x = ""
    for j in  range(1,6):
        if i+j>=6:
            x=x+str(count)
            count+=1
        else:   
             x=x+" "    
    print(x)