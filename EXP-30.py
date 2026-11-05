def encrypt(x, k):
    return (x + k) % 256

def cbc_mac(blocks, k):
    t = 0
    for block in blocks:
        t = encrypt(t ^ block, k)
    return t

k = 10
x = 20

t = cbc_mac([x], k)

second = x ^ t

t2 = cbc_mac([x, second], k)

print("Message X:", x)
print("MAC T:", t)
print("Second Block:", second)
print("Two Block MAC:", t2)
