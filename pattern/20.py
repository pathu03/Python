for i in range(0,4):
    x= ""
    j=1
    reversed = False
    while j > 0:
        
        if j+i==4:
            x = x + '*'
        else:
            x = x+" "

        if reversed==False and j < 4:
            j=j+1
        else:
            reversed=True
            j=j-1

    print(x)