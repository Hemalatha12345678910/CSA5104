p, q = 61, 53
n = p * q
phi = (p-1) * (q-1)

e = 17
d = pow(e, -1, phi)

msg = "HELLO"

encrypted = [pow(ord(ch)-65, e, n) for ch in msg]

print("Plaintext:", msg)
print("Encrypted:", encrypted)

decrypted = ''.join(
    chr(pow(c, d, n) + 65) for c in encrypted
)

print("Decrypted:", decrypted)
