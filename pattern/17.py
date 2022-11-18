i = 1
reverse = False
while i > 0:
    count=1
    x =""
    for j in range(1,6):
        if i+j>=6:
            if reverse==True:
                x=x+str(j)
            else:
                x=x + str(count)
            count+=1
        else:
            x=x+" "

    if i > 4 or reverse == True :
        reverse = True
        i-=1
    else:
        i+=1
       
    print(x)