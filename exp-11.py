

import math

total_keys = math.factorial(25)
log2_keys = math.log2(total_keys)

print("Total possible keys:", total_keys)
print("Approximate power of 2: 2^%.2f" % log2_keys)

# Example equivalence under rotations/reflections:
# If a particular set of 8 geometric transformations
# is treated as equivalent, divide by 8.
unique_keys = total_keys // 8

print("Keys after dividing by 8:", unique_keys)
print("Approximate unique-key power: 2^%.2f" %
      math.log2(unique_keys))
