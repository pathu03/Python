trarvel_log=[
    {
        "country" : "France",
        "visited" : 12,
        "cities"  :["paris","lille","dijon"]
    },
    {
        "country" : "germany",
        "visited" : 5,
        "cities"  :["berlin","hambury","stutart"]
    }
]

def add_new_country(trarvel_country,travel_visited,travel_cities):
    new_country={}
    new_country["country"]= trarvel_country
    new_country["visited"]=travel_visited
    new_country["cities"]=travel_cities
    trarvel_log.append(new_country)

add_new_country("russai",2,["mosco","saint"])
print(trarvel_log)

