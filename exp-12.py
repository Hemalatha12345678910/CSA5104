# Question 12: Hill Cipher Encryption and Decryption

import string

alphabet = string.ascii_lowercase
K = [[9, 4], [5, 7]]

def encrypt(text):
    text = ''.join(ch for ch in text.lower() if ch.isalpha())
    if len(text) % 2:
        text += 'x'

    result = ""
    for i in range(0, len(text), 2):
        x = alphabet.index(text[i])
        y = alphabet.index(text[i + 1])

        c1 = (9 * x + 4 * y) % 26
        c2 = (5 * x + 7 * y) % 26

        result += alphabet[c1] + alphabet[c2]
    return result

def decrypt(cipher):
    # Inverse of K modulo 26
    det = (9 * 7 - 4 * 5) % 26
    det_inv = pow(det, -1, 26)

    inv = [
        [(7 * det_inv) % 26, (-4 * det_inv) % 26],
        [(-5 * det_inv) % 26, (9 * det_inv) % 26]
    ]

    result = ""
    for i in range(0, len(cipher), 2):
        x = alphabet.index(cipher[i])
        y = alphabet.index(cipher[i + 1])

        p1 = (inv[0][0] * x + inv[0][1] * y) % 26
        p2 = (inv[1][0] * x + inv[1][1] * y) % 26

        result += alphabet[p1] + alphabet[p2]
    return result

message = input("Enter plaintext: ")
cipher = encrypt(message)

print("Encrypted text:", cipher)
print("Decrypted text:", decrypt(cipher))
