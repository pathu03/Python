i=1
rev=False
while(i>0):
    x=""
    rev1=False
    j=1
    while(j>0):
        if i+j<=3:
            x=x+str(j)
        else:
            x=x+" "
        if j < 2 and not rev1:
            j+=1
        else:
            if j==2 and not rev1:
                rev1=True
                j=3
            j-=1
    if i < 2 and not rev:
        i+=1
    else:
        if i==2 and not rev:
            rev=True
            i=3
        i-=1
    print(x)