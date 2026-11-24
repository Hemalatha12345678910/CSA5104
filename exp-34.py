
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'12345678'
iv = b'abcdefgh'
data = input("Enter plaintext: ").encode()

p = pad(data, 8)

ecb = DES.new(key, DES.MODE_ECB)
cbc = DES.new(key, DES.MODE_CBC, iv)
cfb = DES.new(key, DES.MODE_CFB, iv, segment_size=8)

e1 = ecb.encrypt(p)
e2 = cbc.encrypt(p)
e3 = cfb.encrypt(data)

print("ECB:", e1.hex())
print("CBC:", e2.hex())
print("CFB:", e3.hex())

print("ECB Decrypt:", unpad(DES.new(key, DES.MODE_ECB).decrypt(e1), 8).decode())
print("CBC Decrypt:", unpad(DES.new(key, DES.MODE_CBC, iv).decrypt(e2), 8).decode())
print("CFB Decrypt:", DES.new(key, DES.MODE_CFB, iv, segment_size=8).decrypt(e3).decode())
