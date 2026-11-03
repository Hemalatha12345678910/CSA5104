# Question 14: Vigenere Cipher with Numerical Key Stream

def encrypt(text, key):
    text = ''.join(ch for ch in text.lower() if ch.isalpha())
    if len(text) != len(key):
        raise ValueError("Key length must equal plaintext length")

    return ''.join(
        chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        for ch, k in zip(text, key)
    )

def decrypt(cipher, key):
    return ''.join(
        chr((ord(ch) - ord('a') - k) % 26 + ord('a'))
        for ch, k in zip(cipher, key)
    )

plaintext = "send more money"
key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

ciphertext = encrypt(plaintext, key)
print("Original plaintext:", plaintext)
print("Ciphertext:", ciphertext)

target = "cash not needed"
target = ''.join(ch for ch in target.lower() if ch.isalpha())

# Derive a key stream that decrypts the same ciphertext to target.
new_key = [
    (ord(c) - ord(p)) % 26
    for c, p in zip(ciphertext, target)
]

print("New key stream:", *new_key)
print("Decrypted with new key:", decrypt(ciphertext, new_key))
