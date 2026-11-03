# Question 18: DES Key Half Demonstration

key56 = input("Enter a 56-bit binary key: ").strip()

if len(key56) != 56 or any(ch not in "01" for ch in key56):
    print("Error: Enter exactly 56 binary bits.")
else:
    C = key56[:28]
    D = key56[28:]

    shifts = [1, 1, 2, 2, 2, 2, 2, 2,
              1, 2, 2, 2, 2, 2, 2, 1]

    print("Initial C0:", C)
    print("Initial D0:", D)

    for round_no, shift in enumerate(shifts, 1):
        C = C[shift:] + C[:shift]
        D = D[shift:] + D[:shift]

        # Each half has 28 bits; PC-2 selects 24 from each.
        # The actual DES PC-2 table must be applied here.
        print(f"Round {round_no:2}: C={C}, D={D}")
