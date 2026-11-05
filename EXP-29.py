state = 1600
block = 1024
lane = 64

capacity = state - block
lanes = capacity // lane

print("Capacity:", capacity)
print("Capacity Lanes:", lanes)

for i in range(1, lanes + 1):
    print("Block", i, ":", i, "lanes updated")

print("Total Blocks:", lanes)
