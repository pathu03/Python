# 
# row=int(input("row:"))
# cols=int(input("cols:"))
# a=[[int(input())for i in range(row)]for j in range (cols)]
# b=[[int(input())for i in range(row)]for j in range (cols)]
# r=[[0 for i in range(row)]for j in range (cols)]
# print(a)
# print(b)
# for i in range(len(a)):
#     for j in range(len(b)):
#         r[i][j]=a[i][j] + b[i][j]
# for z in r:
#     print(z)

# class B:
#     def __init__(self,a):
#         self.a=a
#     def __mul__(self,other):
#         return self.a/other.a
# a=B(6)
# b=B(3)
# z=a*b
# print(z)

# i=1
# rev=False
# while(i>0):
#     j=1
#     x=""
#     rev1=False
#     while(j>0):
#         if i+j<=3:
#             x=x+str(j)
#         else:
#             x=x+" "
#         if j<2 and not rev1:
#             j+=1
#         else:
#             if j==2 and not rev1:
#                 rev1=True
#                 j=3
#             j-=1
#     if i<2 and not rev:
#         i+=1
#     else:
#         if i==2 and not rev:
#             rev=True
#             i=3
#         i-=1
#     print(x)

# class Student:

#     def __init__(self,name,roll_no,mark):
#         self.name=name
#         self.roll_no=roll_no
#         self.mark=mark
    
#     def accept(self,name,roll_no,mark):
#         ob=Student(name,roll_no,mark)
#         Is.append(ob)
#     def display(self,ob):
#         print("namr:",ob.name)
#         print("roll_no:",ob.roll_no)
#         print("mark:",ob.mark)

#     def search(self,rn):
#         for i in range(Is.__len__()):
#             if(Is[i].roll_no==rn):
#                 return i
        
#     def delete(self,rn):
#         i=obj.search(rn)
#         del Is[i]
# Is=[]
# obj=Student("", 0, 0)

# obj.accept("a",1,100)
# obj.accept("b",2,90)
# obj.accept("c",3,80)

# for i in range(Is.__len__()):
#     obj.display(Is[i])

# s=obj.search(2)
# obj.display(Is[s])

# obj.delete(2)
# print(Is.__len__())
# for i in range(Is.__len__()):
#     obj.display(Is[i])

