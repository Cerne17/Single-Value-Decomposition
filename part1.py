from importer import *

def solveSystems(matrix, vector):
    U, s_vector, vh = np.linalg.svd(matrix)

    u_matrix = np.matrix(U)
    s_matrix = np.zeros((len(matrix), len(matrix[0])))
    s_inverse = np.zeros((len(matrix[0]), len(matrix)))
    vh_matrix = np.matrix(vh)

    for i in range(len(s_vector)):
        s_matrix[i, i] = s_vector[i]
        s_inverse[i, i] = 1 / (s_vector[i] if s_vector[i] != 0 else 1)  # To avoid division by zero

    V = vh_matrix.H
    uh = u_matrix.H

    vector_x = V @ s_inverse @ uh @ vector

    return vector_x, u_matrix, s_matrix, vh_matrix

def part1():
    rows =    [3, 4, 3, 4]
    columns = [3, 3, 4, 3]
    ranks =   [3, 3, 3, 2]

    for i in range(4):

        print("----------------")
        print(f"Case {i+1}:")

        row = rows[i]
        column = columns[i]
        rank = ranks[i]

        matrix = RandomMatrixGenerator(row, column, rank).generateRandomMatrix()

        vector = []
        for i in range(column):
            vector.append([random.randint(1, 10)])

        vector = np.array(vector)
        vector.transpose()

        vectorX, u_matrix, s_matrix, vh_matrix = solveSystems(matrix, vector)

        USVh_product = u_matrix @ s_matrix @ vh_matrix
        Ax_product = matrix @ vectorX

        print("Generated Matrix:")
        print(matrix)
        print()

        print("Generated vector: ")
        print(vector)
        print()

        print("Solution: ")
        print(vectorX)
        print()
        
        print("Product A @ x:")
        print(Ax_product)
        print()

        print("Product U @ S @ Vh:")
        print(USVh_product)
        print()

        print("Vector X norm:")
        print(np.linalg.norm(vectorX))
        print()

        print("Compatibility Test: Ax vs. b")
        print(np.allclose(Ax_product, vector, atol=1e-16))
        print()

        print("Compatibility Test: USVh vs. A")
        print(np.allclose(matrix, USVh_product, atol=1e-16))
        print()

        print()

