
import random

text = input("Enter plaintext: ").upper().replace(" ", "")
key = [random.randint(0, 25) for _ in text]

cipher = ""
for i in range(len(text)):
    c = (ord(text[i])-65 + key[i]) % 26
    cipher += chr(c+65)

print("Key:", key)
print("Ciphertext:", cipher)

plain = ""
for i in range(len(cipher)):
    p = (ord(cipher[i])-65-key[i]) % 26
    plain += chr(p+65)

print("Decrypted:", plain)
