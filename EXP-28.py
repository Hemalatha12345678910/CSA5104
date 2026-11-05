q = 23
a = 5

x = 6
y = 15

alice = pow(a, x, q)
bob = pow(a, y, q)

key1 = pow(bob, x, q)
key2 = pow(alice, y, q)

print("Alice Public:", alice)
print("Bob Public:", bob)
print("Alice Key:", key1)
print("Bob Key:", key2)
