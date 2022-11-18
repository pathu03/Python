print("welcome to love calculator")
n1=input("whta is your name?")
n2=input("what is their name?")

combined=n1+n2
lower_case=combined.lower()

t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")


true=t+r+u+a+b+c

l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")

love=l+o+v+e

love_score=str(true) + str(love)

print("love_score :",int(love_score))
love_score=int(love_score)



if love_score<10 or love_score>90:
    print(f"your love score is {love_score},like cock and mentos ")
elif love_score>=40 and love_score<=50:
    print(f"your love score is{love_score},you are alrigt together !")
else:
    print(f"your love score is{love_score}")
