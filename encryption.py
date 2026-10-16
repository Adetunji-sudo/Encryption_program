#importing modules
import string
import random
#creating keywords
char = string.ascii_letters + string.digits + string.punctuation
char = list(char)
key = char.copy()
random.shuffle(key)
#Request code from the user
plaintext = input("Enter the message to encrypt: ")
ciphertext = " "
for chars in plaintext:
    index = char.index(chars)
    ciphertext += key[index]
print(ciphertext)
