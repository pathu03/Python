class User:
    def _init_(self,email,name,password,age):
        self.email = email
        self.name = name
        self.password = password
        self.logged_in = False
        self.age=age

class Customer(User):
    def _init_(self,email,name,password,age):
        self.user_type = 'CUSTOMER'
        super()._init_(email,name,password,age)



class Staff(User):
    def _init_(self,email,name,password,age):
        self.user_type = 'STAFF'
        super()._init_(email,name,password,age)



users = []


while(True):

    print("Enter 1 for Staff\n Enter 2 for Customer")
    type = int(input("option : "))

    if type != 1 and type != 2:
        print("Invalid Input")
        break

    email = str(input("Enter Email"))
    name =str(input("Enter name"))
    password = str(input("Enter password"))
    age = int(input("Enter age"))



    if type == 1:
        user = Staff(email,name,password,age)
        print("Registered Successfully!")
    elif type == 2:
        user = Customer(email,name,password,age)
        print("Registered Successfully!")

    users.append(user)


while(True):

    print("Enter 1 for LOGIN")
    type = int(input("option : "))

    if type != 1:
        break

    print("LOGIN")
    email= str(input("Enter Email : "))
    password = str(input("Enter password : "))

    for user in users:
        if email == user.email:
            if password == user.password:
                user.logged_in = True
            else:
                print("Invalid Password...")

logged_in_users = []
for user in users:
    if user.logged_in:
        data = {
            'name' : user.name,
            'email': user.email,
            'age': user.age,
            'logged_in': user.logged_in,

        }
        logged_in_users.append(data)

print(logged_in_users)


print("Do you want to Logout all")
logout = int(input("1 for logout"))

for user in users:
    if user.logged_in:
        user.logged_in=False

print("logout successfull")

all_users = []
for user in users:
    data = {
        'name': user.name,
        'email': user.email,
        'age': user.age,
        'logged_in': user.logged_in,
    }
    all_users.append(data)



print(all_users)