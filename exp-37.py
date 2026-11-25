
from collections import Counter

text = input("Enter ciphertext: ").upper()
freq = Counter(c for c in text if c.isalpha())

english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
sorted_letters = sorted(freq, key=freq.get, reverse=True)

mapping = dict(zip(sorted_letters, english))

result = ""
for ch in text:
    result += mapping.get(ch, ch)

print("Possible plaintext:", result)
