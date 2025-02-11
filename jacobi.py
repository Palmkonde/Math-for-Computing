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
    
def check_epsilon_vect(pre_x, x_i, epsilon) -> bool:
    res = sum([pre_x[i] - x_i[i] for i in range(len(pre_x))])
    res **= 2

    return res < epsilon 

def solve(A: List[List[int]], b: List[int]) -> None:
    x_i = [i + random.uniform(-0.5, 0.5) for i in x] 
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
    print(it)
    
RANGE_RANDOM = (-5, 5)
if __name__ == "__main__":
    sample_size = 5
    A, b, x = generate_matrix(sample_size, RANGE_RANDOM)
    solve(A, b)
    print(f"Exactly solution: {x}") 
