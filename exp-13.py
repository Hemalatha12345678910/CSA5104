# Question 13: Recover a Hill Cipher Key
# Letters use A=0, B=1, ..., Z=25.

def matrix_inverse_2x2(M):
    a, b = M[0]
    c, d = M[1]
    det = (a * d - b * c) % 26

    if det == 0 or __import__('math').gcd(det, 26) != 1:
        raise ValueError("Plaintext matrix is not invertible modulo 26")

    inv_det = pow(det, -1, 26)
    return [
        [(d * inv_det) % 26, (-b * inv_det) % 26],
        [(-c * inv_det) % 26, (a * inv_det) % 26]
    ]

def multiply(A, B):
    return [
        [(sum(A[i][k] * B[k][j] for k in range(2)) % 26)
         for j in range(2)]
        for i in range(2)
    ]

# Two plaintext blocks form the columns of P.
# Two corresponding ciphertext blocks form the columns of C.
P = [[7, 4], [4, 11]]
C = [[3, 8], [10, 21]]

try:
    K = multiply(C, matrix_inverse_2x2(P))
    print("Recovered key matrix:")
    for row in K:
        print(row)
except ValueError as error:
    print(error)
