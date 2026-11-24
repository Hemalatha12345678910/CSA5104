
import hashlib

p, q, g = 23, 11, 2
x = 3
y = pow(g, x, p)
message = "HELLO"

h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % q

def sign(k):
    r = pow(g, k, p) % q
    s = (pow(k, -1, q) * (h + x*r)) % q
    return r, s

print("Signature 1:", sign(2))
print("Signature 2:", sign(4))
