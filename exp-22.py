# Question 22: S-DES CBC Encryption and Decryption

P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8  = [6, 3, 7, 4, 8, 5, 10, 9]
IP  = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP  = [4, 1, 2, 3, 2, 3, 4, 1]
P4  = [2, 4, 3, 1]

S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def generate_keys(key):
    p = permute(key, P10)
    left, right = p[:5], p[5:]

    left = left_shift(left, 1)
    right = left_shift(right, 1)
    k1 = permute(left + right, P8)

    left = left_shift(left, 2)
    right = left_shift(right, 2)
    k2 = permute(left + right, P8)

    return k1, k2

def xor(a, b):
    return ''.join('1' if x != y else '0'
                   for x, y in zip(a, b))

def sbox(bits, box):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(box[row][col], '02b')

def fk(bits, key):
    left, right = bits[:4], bits[4:]
    expanded = permute(right, EP)
    mixed = xor(expanded, key)

    output = sbox(mixed[:4], S0) + sbox(mixed[4:], S1)
    output = permute(output, P4)

    return xor(left, output) + right

def encrypt_block(block, k1, k2):
    bits = permute(block, IP)
    bits = fk(bits, k1)
    bits = bits[4:] + bits[:4]
    bits = fk(bits, k2)
    return permute(bits, IP_INV)

def decrypt_block(block, k1, k2):
    return encrypt_block(block, k2, k1)

def cbc_encrypt(data, key, iv):
    k1, k2 = generate_keys(key)
    result = []
    previous = iv

    for i in range(0, len(data), 8):
        block = data[i:i + 8]
        mixed = xor(block, previous)
        encrypted = encrypt_block(mixed, k1, k2)
        result.append(encrypted)
        previous = encrypted

    return result

def cbc_decrypt(blocks, key, iv):
    k1, k2 = generate_keys(key)
    result = []
    previous = iv

    for block in blocks:
        decrypted = decrypt_block(block, k1, k2)
        result.append(xor(decrypted, previous))
        previous = block

    return result

key = input("Enter 10-bit key: ").strip()
iv = input("Enter 8-bit IV: ").strip()
plaintext = input("Enter binary plaintext: ").replace(" ", "")

if (len(key) != 10 or set(key) - set("01")
        or len(iv) != 8 or set(iv) - set("01")
        or not plaintext or set(plaintext) - set("01")
        or len(plaintext) % 8 != 0):
    print("Error: Use a 10-bit key, an 8-bit IV, and "
          "binary plaintext in complete 8-bit blocks.")
else:
    encrypted = cbc_encrypt(plaintext, key, iv)
    ciphertext = ''.join(encrypted)

    recovered = ''.join(cbc_decrypt(encrypted, key, iv))

    print("Ciphertext:", ' '.join(
        ciphertext[i:i + 8] for i in range(0, len(ciphertext), 8)))
    print("Decrypted :", ' '.join(
        recovered[i:i + 8] for i in range(0, len(recovered), 8)))
