# class A:
#     def __init__(self,b):
#         self.b=b
#     def __mul__(self,value):
#         return self.b / value.b 
# obj1=A(4)
# obj2=A(2)
# obj3=obj1*obj2
# print(obj3)


# row=int(input("row:"))
# colome=int(input("colome:"))
# a=[[int(input())for c in range(row)]for r in range(colome)]
# b=[[int(input())for c in range(row)]for r in range(colome)]
# z = [[0 for i in range(row)] for j in range(colome)]
# print("a=",a)
# print("b=",b)

# for i in range(len(a)):
#     for j in range(len(b)):
#         z[i][j]=a[i][j] + b[i][j]
# for x in z:
#     print(x)

# i=1
# rev=False
# while(i>0):
#     x=""
#     j=1
#     rev2=False
#     while(j>0):
#         if i+j<=6:
#             x=x+str(j)
#         else:
#             x=x+" "
#         if j<5 and not rev2:
#             j+=1
#         else:
#             if j==5 and not rev2:
#                 rev2=True
#                 j=6
#             j-=1
#     if i<5 and not rev:
#         i+=1
#     else:
#         rev=True
#         i-=1
#     print(x)



# i=1
# rev=False
# while(i>0):
#     j=1
#     x=""
#     rev2=False
#     while(j>0):
#         if i+j<=3:
#             x=x+str(j)
#         else:
#             x=x+" "
#         if j<2 and not rev2:
#             j+=1
#         else:
#             if j==2 and not rev2:
#                 rev2=True
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

class Student:
    def __init__(self,name,rollno,mark):
        self.name=name
        self.rollno=rollno
        self.mark=mark
    def accept(self,name,rollno,mark):
        ob=Student(name,rollno,mark)
        Is.append(ob)
    def display(self,ob):
        print("mame :",ob.name)
        print("rollno:",ob.rollno)
        print("mark:",ob.mark)
    def search(self,rn):
        for i in range(Is.__len__()):
            if (Is[i].rollno==rn):
                return i
    def delet(self,rn):
        i=obj.search(rn)
        del Is[i]
Is=[]
obj=Student("",0,0)
obj.accept("a",1,90)
obj.accept("b",2,95)

for i in range(Is.__len__()):
    obj.display(Is[i])

s=obj.search(2)
obj.display(Is[s])

obj.delet(2)
print(Is.__len__())
for i in range(Is.__len__()):
    obj.display(Is[i])
