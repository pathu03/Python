alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction=input("type 'encode' to encrypt ,type 'decode' to decrypt :\n" )
text=input("type your massage :\n")
shift=int(input("type the shift number :"))


def encrypt(palain_text,shift_amount):
    cipher_text=""
    for letter in palain_text:
        position=alphabet.index(letter)
        new_position=position + shift_amount
        new_letter=alphabet[new_position]
        cipher_text+=new_letter

    print(cipher_text)

def decrypt(palain_text,shift_amount):
    cipher_text=""
    for letter in palain_text:
        position=alphabet.index(letter)
        new_position=position - shift_amount
        new_letter=alphabet[new_position]
        cipher_text+=new_letter

    print(cipher_text)

if direction=="encode":
    encrypt(palain_text=text,shift_amount=shift)
elif direction=="decode":
    decrypt(palain_text=text,shift_amount=shift)