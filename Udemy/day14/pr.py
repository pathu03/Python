from game_data import data
from art import logo,vs
import random
print(logo)
def a(account):
    name_data=account['name']
    description_data=account['description']
    country_data=account['country']
    return f"{name_data} , a {description_data} , from {country_data}"

def check_data(geuss,count_a,count_b):
    if count_a > count_b:
        return geuss=="a"
    else:
        return geuss=="b"
def game():
    game_on=True
    count=0
    account_b=random.choice(data)
    while game_on:
        account_a=account_b
        account_b=random.choice(data)
        
        if account_a==account_b:
            account_b=random.choice(data)
        print(f"user_A : {a(account_a)}")
        print(vs)
        print(f"user_B : {a(account_b)}")

        geuss=input("geuss 'A' or 'B' :").lower()
        count_a=account_a['follower_count']
        count_b=account_b['follower_count']
        is_corect=check_data(geuss,count_a,count_b)
        if is_corect:
            count+=1
            print(f"you right, your score {count}")
        else:
            game_on=False
            print(f"you ronge , final score {count}")
game()

