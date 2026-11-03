# Question 8: Keyword Monoalphabetic Cipher

import string

keyword = "CIPHER"
alphabet = string.ascii_uppercase

cipher_alphabet = ""
for ch in keyword.upper() + alphabet:
    if ch not in cipher_alphabet:
        cipher_alphabet += ch

def encrypt(text):
    result = ""
    for ch in text.upper():
        if ch in alphabet:
            result += cipher_alphabet[alphabet.index(ch)]
        else:
            result += ch
    return result

def decrypt(text):
    result = ""
    for ch in text.upper():
        if ch in cipher_alphabet:
            result += alphabet[cipher_alphabet.index(ch)]
        else:
            result += ch
    return result

print("Plain alphabet :", alphabet)
print("Cipher alphabet:", cipher_alphabet)

message = input("Enter plaintext: ")
encrypted = encrypt(message)

print("Encrypted text:", encrypted)
print("Decrypted text:", decrypt(encrypted))
