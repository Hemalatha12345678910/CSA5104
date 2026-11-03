# Question 21: Padding for Block Cipher Modes

def pad_bits(bits, block_size=8):
    if any(ch not in "01" for ch in bits):
        raise ValueError("Input must contain only 0 and 1")

    # Always append a 1 bit, even when already block-aligned.
    padded = bits + "1"
    zeros = (block_size - len(padded) % block_size) % block_size
    padded += "0" * zeros
    return padded

def remove_padding(bits):
    if "1" not in bits:
        raise ValueError("Invalid padding")
    return bits[:bits.rfind("1")]

plaintext = input("Enter binary plaintext: ")
block_size = int(input("Enter block/segment size: "))

padded = pad_bits(plaintext, block_size)

print("Original:", plaintext)
print("Padded:", padded)
print("Blocks:", [padded[i:i + block_size]
                   for i in range(0, len(padded), block_size)])
print("Recovered:", remove_padding(padded))
