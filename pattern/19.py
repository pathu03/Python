i = 1
rev1 = False
while(i > 0):
    x = ''

    rev2=False
    j=1
    while(j > 0):
        if i+j<=6:
            x=x+str(j)
        else:
            x=x+" "
        if j < 5 and not rev2:
            j+=1
        else:
            if j == 5 and not rev2:
                rev2=True
                j = 6
            j-=1
    if i < 5 and not rev1:
        i+=1
    else:
        rev1 = True
        i-=1
    print(x)
    
   