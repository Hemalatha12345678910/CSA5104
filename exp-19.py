# Question 19: 3DES CBC Mode

from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

key = bytes.fromhex("0123456789ABCDEFFEDCBA9876543210")
iv = bytes.fromhex("1234567890ABCDEF")

plaintext = input("Enter message: ").encode()

cipher = DES3.new(key, DES3.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, 8))

print("Ciphertext:", ciphertext.hex().upper())

decipher = DES3.new(key, DES3.MODE_CBC, iv)
recovered = unpad(decipher.decrypt(ciphertext), 8)

print("Decrypted:", recovered.decode())
