import random
word_list=["ardvark","baboon","camel"]

chosen_word=random.choice(word_list)

guss=input("guess a letter:").lower()


for letter in chosen_word:
    if letter==guss:
        print("right")
    else:
        print("wrong")