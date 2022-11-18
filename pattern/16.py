i = 1
reverse = False
while i > 0:
    x =""
    for j in range(i,0,-1):
        x=x + str(j)

    if i > 4 or reverse == True :
        reverse = True
        i-=1
    else:
        i+=1
    print(x)