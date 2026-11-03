# Question 17: DES Encryption and Decryption

from Crypto.Cipher import DES

key = bytes.fromhex("133457799BBCDFF1")
plaintext = bytes.fromhex("0123456789ABCDEF")

cipher = DES.new(key, DES.MODE_ECB)

ciphertext = cipher.encrypt(plaintext)
decrypted = cipher.decrypt(ciphertext)

print("Plaintext :", plaintext.hex().upper())
print("Ciphertext:", ciphertext.hex().upper())
print("Decrypted :", decrypted.hex().upper())
