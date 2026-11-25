
from collections import Counter

text = input("Enter ciphertext: ").upper()

english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
freq = Counter(c for c in text if c.isalpha())

sorted_letters = sorted(freq, key=freq.get, reverse=True)

print("Top 10 possible plaintexts:")

for shift in range(10):
    mapping = {}
    for i, ch in enumerate(sorted_letters):
        mapping[ch] = english[(i+shift) % 26]

    result = ""
    for ch in text:
        result += mapping.get(ch, ch)

    print(shift+1, result)
