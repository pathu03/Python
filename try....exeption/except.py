try :
    x=int(input("enter number"))
except ValueError:
    x=9
except:
    x=8
print(x)