# Question 16: Monoalphabetic Frequency Attack

import string
from collections import Counter

ciphertext = input("Enter ciphertext: ").lower()
top_n = int(input("How many results? "))

english_order = "etaoinshrdlcumwfgypbvkjxqz"

counts = Counter(ch for ch in ciphertext if ch in string.ascii_lowercase)
cipher_order = ''.join(ch for ch, _ in counts.most_common())

mapping = {
    cipher_order[i]: english_order[i]
    for i in range(min(len(cipher_order), 26))
}

guess = ''.join(mapping.get(ch, ch) for ch in ciphertext)

print("\nFrequency-based plaintext guess:")
print(guess)

print("\nNote: This is a heuristic guess, not guaranteed decryption.")
print("Requested number of candidates:", top_n)
