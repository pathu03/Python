import random
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
nubers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','*','+','-','/','?','|']

nr_letters=int(input("how many letters would you like in you password?\n"))
nr_numbers=int(input("how many number would you?\n"))
nr_symbols=int(input("how many numbers would you like?"))
#hard password
password_list=[]

for char in range(1,nr_letters +1):
    password_list.append(random.choice(letters))

for char in range(1,nr_numbers +1):
    password_list.append(random.choice(nubers))

for char in range(1,nr_symbols +1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+=char
print(password)

#eazy password

# password=""

# for char in range(1,nr_letters +1):
#     password+=(random.choice(letters))

# for char in range(1,nr_numbers +1):
#     password+=(random.choice(nubers))

# for char in range(1,nr_symbols +1):
#     password+=(random.choice(symbols))

# print(password)
