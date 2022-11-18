i =1
for i in range(1,6):
    x= ""
    j=1
    reversed = False
    while j > 0:
        
        if j>i:
            x = x + " "
        else:
            x = x+str(j)

        if reversed==False and j < 5:
            j=j+1
        else:
            if reversed == False:
                j = 6
            reversed=True
            j=j-1

    print(x)