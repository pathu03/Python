alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction=input("type 'encode' to encrypt ,type 'decode' to decrypt :\n" )
text=input("type your massage :\n")
shift=int(input("type the shift number :"))


def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount*= -1
    for letter in start_text:
        position=alphabet.index(letter)
        new_position=position +shift_amount
        end_text+= alphabet[new_position]

    print(f"here the{direction}d result:{end_text}")
caesar(start_text=text,shift_amount=shift,cipher_direction=direction)