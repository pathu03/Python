row=int(input("row:"))
colome=int(input("colome:"))
a=[[int(input())for c in range(row)]for r in range(colome)]
b=[[int(input())for c in range(row)]for r in range(colome)]
z = [[0 for i in range(row)] for j in range(colome)]
print("a=",a)
print("b=",b)

for i in range(len(a)):
    for j in range(len(b)):
        z[i][j]=a[i][j] + b[i][j]
for x in z:
    print(x)