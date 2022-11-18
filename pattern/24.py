i=1
for i in range(1,6):
    x=""
    j=1
    count=5
    reversed=False
    while j>0:
        if j<5 and reversed==False :
            if i+j>=6:
                x=x+str(count)
                count-=1
            else:
                x=x+" "
            j+=1
        else:
            reversed=True
            j-=1
            if i+j>=5:
                x=x+str(count)
                count+=1
            else:
                x=x+" "
    print(x)
