import random


def generate_matrix():
    N = 2
    M = []

    for i in range(N):
        R = []
        for j in range(N):
            R.append(random.randint(1, 5))
        M.append(R)
    
    real_solution = [random.randint(1, 5) for i in range(N)]

    b = []
    for i in range(2):
        res = 0
        for j in range(2):
            res += M[i][j] * real_solution[j]
        b.append(res)
    
    return M, b

if __name__ == "__main__":
    matrix, answer = generate_matrix()
    
    print(f"This is LHS: {matrix}")
    print(f"This is RHS: {answer}")

    solved = False
    while not solved:
        x = []
        for i in range(2):
            x.append(int(input(f"Enter x{i}: ")))
        
        print(f"This your solution {x}")
        b = []
        for i in range(2):
            res = 0
            for j in range(2):
               res += matrix[i][j] * x[j]
            b.append(res)
        
        print(f"This is your answer {b}")

        if b == answer:
            print("Correct!")
            solved = True
        
        if b[0] != answer[0]:
            print("Your first answer is wrong")
        if b[1] != answer[1]:
            print("Your second answer is wrong")