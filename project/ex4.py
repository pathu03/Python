rows=int(input("enter the rows"))
cols=int(input("enter the cols"))
x=[[int(input())for i in range(rows)for j in range(cols)]]
y=[[int(input)for i in range(rows)for j in range(cols)]]
result=[[0 for i in range(rows)for j in range(cols)]]
for i in range(len(x)):
    for j in range(len(y)):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)