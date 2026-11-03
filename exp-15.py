# Question 15: Additive Cipher Frequency Attack

import string

alphabet = string.ascii_lowercase
english_frequency = "etaoinshrdlcumwfgypbvkjxqz"

def decrypt(cipher, shift):
    result = ""
    for ch in cipher.lower():
        if ch in alphabet:
            result += alphabet[(alphabet.index(ch) - shift) % 26]
        else:
            result += ch
    return result

def score(text):
    letters = [ch for ch in text if ch in alphabet]
    if not letters:
        return 0

    counts = {ch: letters.count(ch) for ch in alphabet}
    return sum(
        counts[ch] * (26 - i)
        for i, ch in enumerate(english_frequency)
    )

ciphertext = input("Enter ciphertext: ")
top_n = int(input("How many results? "))

results = []
for shift in range(26):
    text = decrypt(ciphertext, shift)
    results.append((score(text), shift, text))

results.sort(reverse=True)

for rank, (value, shift, text) in enumerate(results[:top_n], 1):
    print(f"{rank}. Shift={shift}: {text}")
