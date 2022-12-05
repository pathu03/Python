print("welcome to love calculator")
n1=input("whta is your name?")
n2=input("what is their name?")

combined=n1+n2
lower_case=combined.lower()

t=lower_case.count("r")
r=lower_case.count("v")
u=lower_case.count("a")
e=lower_case.count("i")


true=t+r+u+e

l=lower_case.count("l")
o=lower_case.count("a")
v=lower_case.count("s")
e=lower_case.count("n")

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
