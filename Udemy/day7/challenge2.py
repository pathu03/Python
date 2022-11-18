import random
word_list=["ardvark","baboon","camel"]

chosen_word=random.choice(word_list)
print(f'the solution is {chosen_word}')

display=[]
word_length=len(chosen_word)
for _ in range(word_length):
    display+="_"
print(display)
guss=input("guess a letter:").lower()


for position in range(word_length):
    letter=chosen_word[position]
    if letter==guss:
        display[position]=letter

print(display)