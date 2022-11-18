x=[[1,2,3],
   [4,5,6],
   [7,8,9]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(x)):
    for j in range(len(x)):
        result[i][j]=x[j][i]
for r in result:
    print(r)