# Question 10: Playfair Cipher Encryption

matrix = [
    list("MFHIK"),
    list("UNOPQ"),
    list("ZVWXY"),
    list("ELARG"),
    list("DSTBC")
]

def encrypt_playfair(message):
    positions = {}
    for r in range(5):
        for c in range(5):
            positions[matrix[r][c]] = (r, c)

    text = "".join(ch for ch in message.upper() if ch.isalpha())
    text = text.replace("J", "I")

    # Prepare pairs, inserting X between repeated letters
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        if i + 1 >= len(text):
            b = "X"
            i += 1
        elif text[i + 1] == a:
            b = "X"
            i += 1
        else:
            b = text[i + 1]
            i += 2
        pairs.append((a, b))

    result = ""

    for a, b in pairs:
        r1, c1 = positions[a]
        r2, c2 = positions[b]

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result

message = input("Enter plaintext: ")
print("Ciphertext:", encrypt_playfair(message))
