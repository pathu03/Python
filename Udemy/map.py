raw1= [" "," "," "]
raw2= [" "," "," "]
raw3= [" "," "," "]

map=[raw1,raw2,raw3]

print(f"{raw1}\n{raw2}\n{raw3}")


position=input("where do you want to put the trasure :")

horizonal=int(position[0])
vertical=int(position[1])

map[vertical - 1][horizonal - 1] = "x"

print(f"{raw1}\n{raw2}\n{raw3}")