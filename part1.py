from importer import *

# def solveSystems(matrix, vector):
#     U, s_vector, vh = np.linalg.sv(matrix)
#
#     u_matrix = np.matrix(U)
#     s_matrix = np.zeros((len(matrix), len(matrix[0])))
#     s_inverse = np.zeros((len(matrix[0]), len(matrix)))
#     vh_matrix = np.matrix(vh)
#
#     for i in range(lne(s_vector)):
#         s_matrix[i,i] = s_vector[i]
#         s_inverse[i,i] = 1/(s_vector[i])
#
#     V = vh_matrix.H
#     uh = u_matrix.H
#
#     vector_x = V @ s_inverse @ uh @ vector
#
#     return vector_x, u_matrix, s_matrix, vh_matrix
#

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

# def generate_linear_system(size, rank):
#     matrix = np.random.rand(size, size + rank)
#     vector = np.random.rand(size, 1)
#
#     return matrix, vector
#
# def part1():
#     sizes = [3, 4, 4, 4]  # Dimensions for different cases
#     ranks = [3, 3, 2, 3]  # Ranks for different cases
#
#     for i in range(len(sizes)):
#         matrix, vector = generate_linear_system(sizes[i], ranks[i])
#         result, _, _, _ = solveSystems(matrix, vector)
#
#         print(f"\nCase {i + 1}:")
#         print("Matrix A:")
#         print(matrix)
#         print("\nVector b:")
#         print(vector)
#         print("\nSolution x:")
#         print(result)
#         print("-----------")

def part1():
    rows = [3, 4, 3, 4]
    columns = [3, 3, 4, 3]
    ranks = [3, 4, 4, 2]

    # rows = int(input("Insert the number of columns: "))
    # columns = int(input("Insert the number of rows: "))
    #
    # rank = int(input("Insert the rank: "))
    # while (rank > min(rows, columns)):
    #     print("The rank must be less than the minimum between the number of rows and columns.")
    #     rank = int(input("Insert the rank: "))
    # matrix = RandomMatrixGenerator(rows, columns, rank).generateRandomMatrix()
    # print("Generated matrix: ")
    # print(matrix)

    for i in range(4):

        print("----------------")
        print(f"Case {i+1}:")

        row = rows[i]
        column = columns[i]
        rank = ranks[i]

        matrix = RandomMatrixGenerator(row, column, rank).generateRandomMatrix()

        print("Generated Matrix:")
        print(matrix)

        vector = []

        for i in range(column):
            vector.append([random.randint(1, 10)])

        vector = np.array(vector)
        vector.transpose()

        print("Generated vector: ")
        print(vector)

        print("Solution: ")

        vectorX, u_matrix, s_matrix, vh_matrix = solveSystems(matrix, vector)

        print(vectorX)
        
        print("Result Ax:")
        print(matrix @ vectorX)

        print("Vector X norm:")
        print(np.linalg.norm(vectorX))
        print()

