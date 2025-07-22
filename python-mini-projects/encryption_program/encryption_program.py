import random
import string

characters = " " + string.punctuation + string.digits + string.ascii_letters
characters = list(characters)

encrypted_symbols = characters.copy()
random.shuffle(encrypted_symbols)

print()

#ENCRYPTION
plain_text = input("Enter Message to be encrypted: ")
encrypted_text = ""
for letter in plain_text:
    index = characters.index(letter)
    encrypted_text += encrypted_symbols[index]
print(f"Your Text: {plain_text}")
print(f"Encrypted Text: {encrypted_text}")


#DECRYPTION
encrypted_text = input("Enter Message to be Decrypted: ")
plain_text = ""

for letter in encrypted_text:
    index = encrypted_symbols.index(letter)
    plain_text += characters[index]
print(f"Your Text: {encrypted_text}")
print(f"Decrypted Text: {plain_text}")

