
import math

text = input("Enter plaintext: ").upper()
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if math.gcd(a, 26) != 1:
    print("Invalid key: a must be coprime with 26")
else:
    cipher = ""
    for ch in text:
        if ch.isalpha():
            p = ord(ch)-65
            cipher += chr((a*p+b)%26+65)
        else:
            cipher += ch

    print("Ciphertext:", cipher)
