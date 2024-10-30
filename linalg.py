from sympy import *
from numpy import *
init_printing(use_unicode=True)

print("Tools:")
print("1. Cross product")
print("2. Dot product")
print("3. Matrix multiplication")
print("4. Reduced row echelon form")
print("5. Matrix to LaTeX")
n = int(input("Enter tool number: "))

# reduced row echelon form
if n == 1:
    print("Input format: enter vectors separated by spaces and in the form a b c")
    print("To finish entering vectors, press Enter twice")
    while True:
        vectors = []
        while True:
            vector = input("")
            if vector == "":
                break
            vector = vector.split(" ")
            vectors.append(Matrix(vector))
        for i in range(1, len(vectors)):
            if len(vectors) == 1:
                break
            if vectors[i-1] == vectors[i]:
                vectors = [Matrix([0, 0, 0])]
                break
            try:
                vectors.insert(0, vectors[i-1].cross(vectors[i]))
            except:
                print("Invalid vectors\n")
                vectors = []
                break
            vectors.pop(i)
            vectors.pop(i)
            i = i-1
        pprint(vectors[0])
        print("Enter new vectors:")
elif n == 2:
    print('fuck you')
elif n == 3:
    while True:
        print("Matrix 1:")
        mat1 = []
        while True:
            row = input("")
            if row == "exit":
                exit()
            if row == "":
                break
            row = row.split(" ")
            mat1.append(row)
        print("Matrix 2:")
        mat2 = []
        while True:
            row = input("")
            if row == "exit":
                exit()
            if row == "":
                break
            row = row.split(" ")
            mat2.append(row)
        pprint(Matrix(mat1)*Matrix(mat2))
elif n == 4:
    print("Input format: enter rows separated by new lines and in the form a b c d")
    print("To finish entering rows, press Enter twice")
    while True:
        matrix = []
        while True:
            row = input("")
            if row == "exit":
                exit()
            if row == "":
                break
            row = row.split(" ")
            matrix.append(row)
        try:
            rref_matrix = (Matrix(matrix).rref())
            pprint(rref_matrix[0])
            print("Pivot columns:", rref_matrix[1], "\n")
        except:
            print("Invalid matrix\n")
        print("Enter new matrix:")

