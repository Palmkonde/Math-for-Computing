import random

from typing import Tuple, List

def generate_matrix(
        N: int, 
        range_input: Tuple[int, int]
) -> Tuple[List[List[int]], List[int], List[int]]:

    start, end = range_input[0], range_input[1]
    x = [random.randint(start, end) for _ in range(N)]

    A = [[(i + j + 1) for j in range(N)] for i in range(N)]
    for i in range(N):
        A[i][i] = sum(A[i]) + 1

    b = [sum(A[i][j] * x[j] for j in range(N)) for i in range(N) ]

    return A, b, x

def generate_hilbert_martix(
    N: int,
    x_input: List[int]
) -> Tuple[List[List[int]], List[int], List[int]]:

    A = [[1/(i + j + 1) for j in range(N)] for i in range(N)]
    b = [sum(A[i][j] * x_input[j] for j in range(N)) for i in range(N) ]

    return A, b, x
    
def check_epsilon_vect(pre_x, x_i, epsilon) -> bool:
    res = sum([pre_x[i] - x_i[i] for i in range(len(pre_x))])
    res **= 2

    return res < epsilon

def solve_jacobi(A: List[List[int]], b: List[int], x_solution) -> int:
    x_i = [i + random.uniform(-0.5, 0.5) for i in x_solution] 
    LHS = A.copy()   
    RHS = b.copy()

    it = 0
    while it <= 100:
        tmp_xi = x_i.copy()
        for row in range(len(LHS)):
            tmp = LHS[row][row]
            res = 0
            for col in range(len(LHS)):
                if row == col: continue
                res += tmp_xi[col] * LHS[row][col]
            x_i[row] = (RHS[row] - res) / tmp

        it += 1
        print(x_i)
        if check_epsilon_vect(tmp_xi, x_i, epsilon=1e-10):
            break
    return it
    
def solve_Seidal(A: List[List[int]], b: List[int], x_solution) -> int:
    x_i = [i + random.uniform(-0.5, 0.5) for i in x_solution] 
    LHS = A.copy()   
    RHS = b.copy()

    it = 0
    while it <= 100:
        tmp_xi = x_i.copy()
        for row in range(len(LHS)):
            tmp = LHS[row][row]
            res = 0
            for col in range(len(LHS)):
                if row == col: continue
                res += x_i[col] * LHS[row][col]
            x_i[row] = (RHS[row] - res) / tmp

        it += 1
        print(x_i)
        if check_epsilon_vect(tmp_xi, x_i, epsilon=1e-10):
            break
    return it

RANGE_RANDOM = (-5, 5)
if __name__ == "__main__":
    sample_size = 5
    A, b, x = generate_matrix(sample_size, RANGE_RANDOM)
    A_hill, b_hill, x_hill = generate_hilbert_martix(sample_size, x)

    print("Start Jacobi")
    it1 = solve_jacobi(A, b, x)
    print("End Jacobi\n")
    
    print("Start Seidal")
    it2 = solve_Seidal(A, b, x)
    print("End Seidel\n")

    print(f"Exactly solution: {x}") 
    print(f"iterations from jacobi: {it1}")
    print(f"iterations from seidel: {it2}")
