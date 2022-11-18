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
obj.accept("c",3,70)
obj.accept("d",4,65)

for i in range(Is.__len__()):
    obj.display(Is[i])

s=obj.search(2)
obj.display(Is[s])

obj.delet(2)
print(Is.__len__())
for i in range(Is.__len__()):
    obj.display(Is[i])