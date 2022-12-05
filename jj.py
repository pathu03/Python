n=int(input())
array=[int(input())for i in range(n)]
print(array)
right=array[-1]
left=[0]
max=max(right,left)


while(right>left):
    z=max-array
    array+=1



