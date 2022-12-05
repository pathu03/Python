def a():
    file_name=input("entr you name :")
    z=file_name
    return z
b=a()
file1 = open(b, "w" )
file1.write(" name=pathu,\n age=20,\n number=7600961401,\n bod=11/08/2002,\n cours=python")
file1.close()
file1 = open(a() , "r" )
file1=file1.read()
print(file1)



