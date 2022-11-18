
a=[1,20,30,40,50]
print(a)
print("select 1 for insert the number")
print("select 2 for delete the number")
print("select 3 for update the number")
select=int(input("select your element :"))

if select==1:
    a.append(int(input("insert your number :")))
elif select==2:
    a.remove(int(input("delete your number :")))
elif select==3:
    x=int(input("enter your replcing number :"))
    y=int(input("enter your replced number :"))
    for i in range(len(a)):
        if a[i]==x:
            a[i]=y
print(a)
