import random

from typing import List, Tuple

MIN_RANGE, MAX_RANGE = -5, 5

def printM(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()

def generate_matrix(size: int) -> Tuple[List[List[int]], List[int]]:
    A = []
    random_number = None
    for _ in range(size):
        tmp = []
        for _ in range(size):
            random_number = random.randint(MIN_RANGE, MAX_RANGE)
            tmp.append(random_number)
        A.append(tmp)

    x = []
    for i in range(size):
        random_number = random.randint(MIN_RANGE, MAX_RANGE)
        x.append(random_number)

    # Ax = b
    solution = []
    for i in range(size):
        res = 0
        for j in range(size):
            res += A[i][j] * x[j]

        solution.append(res)

    return A, solution


def solve(A: List[List[int]], b: List[int]) -> List[int]:
    matrix = A

    # Reform
    for row in range(len(matrix)):
        matrix[row].append(b[row])

    col, row = 0, 0
    while col < (len(matrix[0]) - 1) and row < len(matrix):
        if row == col and matrix[row][col] == 0:
            for i in range(len(matrix)):
                if matrix[i][col] != 0:
                    matrix[i], matrix[col] = matrix[col], matrix[i]

        if matrix[row][col] != 0:
            tmp = matrix[row][col]
            for j in range(col, len(matrix[0]) ):
                matrix[row][j] = matrix[row][j] / tmp
            
            for j in range(row+1, len(matrix)):
                matrix[j][col] = matrix[j][col] + (matrix[row][col] * matrix[j][col] * -1)
        
        col += 1
        row += 1
        
    print(f"Matrix is")
    printM(matrix)

if __name__ == "__main__":
    A, b = generate_matrix(3)
    solve(A, b)
