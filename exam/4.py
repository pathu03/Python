class B:
    def __init__(self,a):
        self.a=a
    def __mul__(self,other):
        return self.a/other.a
a=B(int(input()))
b=B(int(input()))
z=a*b
print(z)