
text = input("Enter ciphertext: ").upper()

english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

results = []

for key in range(26):
    plain = ""
    for ch in text:
        if ch.isalpha():
            plain += chr((ord(ch)-65-key)%26+65)
        else:
            plain += ch

    score = sum(english.index(c) if c in english else 26
                for c in plain if c.isalpha())

    results.append((score, key, plain))

results.sort()

for score, key, plain in results[:10]:
    print("Key:", key, "Plaintext:", plain)
