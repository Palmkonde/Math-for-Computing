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

    return A, x, solution


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
                k = (matrix[row][col] * matrix[j][col] * -1)
                for sub_col in range(col, len(matrix[0])):
                    matrix[j][sub_col] += k * (matrix[row][sub_col])
        
        col += 1
        row += 1

    print("After do forward step") 
    printM(matrix)
    col -= 1
    row -= 1
    while col >= 0 and row >= 0:
        for j in range(row-1, -1, -1):
            k = (matrix[row][col] * matrix[j][col] * -1)
            for sub_col in range(col, len(matrix[0])):
                matrix[j][sub_col] += k * (matrix[row][sub_col])
        col -= 1
        row -= 1
     
    print(f"After do backward step")
    printM(matrix)
    
    many_sol = True
    for r in range(len(matrix)):
        for c in range(len(matrix[0]) - 1):
            if matrix[r][c] != 0:
                many_sol = False
                break
                
        if many_sol:
            print("There's exist zeros row, therefore there's many solution")
            return None

    answer = []
    for row in range(len(matrix)):
       answer.append(matrix[row][-1]) 
    return answer

def check_error(matrix: List[int], solution: List[int]) -> List[int]:
    error = []
    for i in range(len(matrix)):
        error.append(abs(matrix[i] - solution[i]))
    
    return error

def cal_MSE(error: List[int]) -> float:
    N = len(error)
    result = sum([i**2 for i in error]) / N
    return result

if __name__ == "__main__":
    A, real_answer, b = generate_matrix(5)
    answer = solve(A, b)
    
    if not answer:
        exit(0) 
    
    error = check_error(real_answer, answer)
    error_mean_square = cal_MSE(error)
    
    print(f"real answer is {real_answer}")
    print(f"We got {answer}")
    print(f"This is error matrix {error}")
    print(f"MSE is equal to {error_mean_square}")