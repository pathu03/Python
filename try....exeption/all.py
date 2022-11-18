try:
    x=int(input("enter number :"))
except:
    x=10
else:
    print("else")
finally:
    print("final")
print(x)