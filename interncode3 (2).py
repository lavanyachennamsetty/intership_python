import numpy as np
def read_matrix(name):
    r = int(input(f"Enter rows of {name}: "))
    c = int(input(f"Enter columns of {name}: "))
    print(f"Enter elements of {name} row-wise:")
    data = list(map(float, input().split()))
    matrix = np.array(data).reshape(r, c)
    return matrix

print("Matrix Operations Tool")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose")
print("5. Determinant")

choice = int(input("Choose operation: "))

if choice in [1, 2, 3]:
    A = read_matrix("Matrix A")
    B = read_matrix("Matrix B")

    if choice == 1:
        print("Result:\n", np.add(A, B))

    elif choice == 2:
        print("Result:\n", np.subtract(A, B))

    elif choice == 3:
        print("Result:\n", np.matmul(A, B))

elif choice == 4:
    A = read_matrix("Matrix")
    print("Transpose:\n", np.transpose(A))

elif choice == 5:
    A = read_matrix("Matrix (Square only)")
    print("Determinant:", np.linalg.det(A))

else:
    print("Invalid choice")