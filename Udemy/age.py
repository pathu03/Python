age=int(input("enter your age :"))

years= 90 - age
day  = years * 365
week = years * 52
month= years * 12

message=(f"you have {day} day,\n{week} week,\n{month} month ")

print(message)