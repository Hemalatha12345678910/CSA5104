p, q = 17, 11
n = p * q
phi = (p-1) * (q-1)

e = 7
d = pow(e, -1, phi)

msg = 20
c = pow(msg, e, n)
m = pow(c, d, n)

print("Public Key:", e, n)
print("Private Key:", d, n)
print("Encrypted:", c)
print("Decrypted:", m)

print("Is new key safe with same n? No")
