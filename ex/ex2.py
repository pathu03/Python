tarvel_bus_log=[
    {
        "bus": ["mini_bus","volvo","sleeper"],

        "total_trip":[{"mini_bus" :"20 trip","volvo":"15 trip","sleeper":"9 trip"}],
        
        "mini_bus" :[{"1":"pathu","2":"romil","3":"sahil","4":"jay","5":"","6":"","7":"jay","8":"","9":"ravi","10":"keval",
                    "11":"kishan","12":"","13":"","14":"darshit","15":"","16":"anant","17":"ronak","18":"","19":"","20":""},{"date":"25 nov","time":"9:30"}],
                    


        "volvo":   [{"1":"keval","2":"ravi","3":"jay","4":"","5":"","6":"","7":"romil","8":"","9":"darshit","10":"ravi",
                    "11":"sahil","12":"","13":"","14":"ronak","15":"","16":"savan","17":"jay","18":"","19":"","20":"",
                    "21":"nik","22":"kano","23":"sagar","24":"pooja","25":"jinal","26":"","27":"hsati","28":"bani","29":"janam","30":"jd",
                    "31":"","32":"trisha"},{"date":"25 nov","time":"13:20"}],


        "sleeper":[{"1":"pathu,ravi","2":"romil,sahil","3":"jay,ronak","4":" ","5":"magan,chagan","6":"chirag,lalo","7":"raju,chandu","8":"","9":"raviraj,bhumi","10":"keval",
                    "11":"kishan","12":"","13":"","14":"darshit","15":"jd","16":"anant","17":"ronak","18":" ","19":"","20":"trisha"},
                    {"time":"04:30"},{"time":"15:15"}],
    }
]
for i in tarvel_bus_log:
    print(i["bus"])
    print(i["total_trip"])
a=input("select your bus:")
if a=="mini_bus":
    print(i["mini_bus"])
elif a=="volvo":
    print(i["volvo"])
elif a=="sleeper":
    print(i["sleeper"])
else:
    print("not valid")

