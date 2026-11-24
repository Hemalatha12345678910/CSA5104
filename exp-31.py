
def shift(block, R):
    msb = block[0] >> 7
    value = (int.from_bytes(block, 'big') << 1)
    value &= (1 << (len(block)*8)) - 1
    result = value.to_bytes(len(block), 'big')

    if msb:
        result = bytes([result[0] ^ R]) + result[1:]
    return result

def cmac_keys(L, R):
    K1 = shift(L, R)
    K2 = shift(K1, R)
    return K1.hex(), K2.hex()

n = int(input("Block size (64 or 128): "))
L = bytes(n // 8)
R = 0x1B if n == 64 else 0x87

K1, K2 = cmac_keys(L, R)
print("K1:", K1)
print("K2:", K2)
