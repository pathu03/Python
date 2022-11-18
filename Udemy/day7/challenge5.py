import random

from hangman_words import word_list
choesn_word=random.choice(word_list)
world_length=len(choesn_word)

end_of_game=False
lives=6

from hangman_art import logo,stages
print(logo)

display=[]
for _ in range(world_length):
    display+="_"

while not end_of_game:
    guess=input("guess a letter :").lower()

    if guess in display:
        print(f"you've already guessed {guess}")

    for position in range(world_length):
        letter=choesn_word[position]
        if letter==guess:
            display[position]=letter

    if guess not in choesn_word:
        print(f"you guess {guess}, thats not in the word. you lose a life.")
        lives-=1
        if lives==0:
            end_of_game=True
            print("you lose")

    print(f"{' '. join(display)}")

    if "_" not in display:
        end_of_game=True
        print("you win")

    print(stages[lives])