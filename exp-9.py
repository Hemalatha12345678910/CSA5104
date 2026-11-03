# Question 9: Playfair Cipher Decryption

def make_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")
    letters = ""

    for ch in key + alphabet:
        if ch in alphabet and ch not in letters:
            letters += ch

    return [list(letters[i:i + 5]) for i in range(0, 25, 5)]

def decrypt_playfair(ciphertext, matrix):
    positions = {}
    for r in range(5):
        for c in range(5):
            positions[matrix[r][c]] = (r, c)

    text = "".join(ch for ch in ciphertext.upper() if ch.isalpha())
    text = text.replace("J", "I")
    result = ""

    for i in range(0, len(text) - 1, 2):
        a, b = text[i], text[i + 1]
        r1, c1 = positions[a]
        r2, c2 = positions[b]

        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result

key = input("Enter Playfair keyword: ")
ciphertext = """
KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ
"""

matrix = make_matrix(key)

print("Key matrix:")
for row in matrix:
    print(" ".join(row))

print("Decrypted text:", decrypt_playfair(ciphertext, matrix))
