class B:
    def __init__(self,a):
        self.a=a
    def __mul__(self,other):
        return self.a/other.a
a=B(6)
b=B(3)
z=a*b
print(z)