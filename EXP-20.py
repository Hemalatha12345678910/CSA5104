# Question 20: Demonstrate CBC XOR Error Propagation

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Demonstration of the CBC decryption relationship:
# P[i] = D(C[i]) XOR C[i-1]
# For block 1, C[0] is the initialization vector.

P1 = bytes.fromhex("41424344")
P2 = bytes.fromhex("45464748")
P3 = bytes.fromhex("494A4B4C")

IV = bytes.fromhex("00000000")

# Illustrative block values, not a real block-cipher encryption
D_C1 = xor_bytes(P1, IV)
D_C2 = xor_bytes(P2, bytes.fromhex("11111111"))
D_C3 = xor_bytes(P3, bytes.fromhex("22222222"))

# Correct CBC plaintext recovery
recovered_P2 = xor_bytes(D_C2, bytes.fromhex("11111111"))

print("Original P2:", P2.hex().upper())
print("Recovered P2:", recovered_P2.hex().upper())

# Flip one bit in the preceding ciphertext block.
changed_C1 = bytes.fromhex("11111110")
changed_P2 = xor_bytes(D_C2, changed_C1)

print("P2 after C1 bit error:", changed_P2.hex().upper())
