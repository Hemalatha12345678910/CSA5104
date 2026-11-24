
from Crypto.Cipher import DES

key = b'12345678'
text = input("Enter plaintext: ").encode()

pad = 8 - len(text) % 8
text += bytes([pad]) * pad

cipher = DES.new(key, DES.MODE_ECB)
encrypted = cipher.encrypt(text)
decrypted = cipher.decrypt(encrypted)

print("Encrypted:", encrypted.hex())
print("Decrypted:", decrypted[:-decrypted[-1]].decode())
