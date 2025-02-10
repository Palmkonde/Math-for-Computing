import random

from typing import List, Tuple

MIN_RANGE, MAX_RANGE = -5, 5

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

if __name__ == "__main__":
    print(generate_matrix(2))