import numpy as np
import matplotlib.pyplot as plt

from typing import Tuple, List

def f(x: int) -> None:
    return np.sin(9*x) 

def generate_data(range_input: Tuple[int, int], m):
    a, b = range_input[0], range_input[1]
    x_i = [np.random.uniform(a, b) for _ in range(m)]
    y_i = [f(x_subs) for x_subs in x_i]

    return range_input, x_i, y_i

def interpolate(range_input, x_i, y_i, m) -> None:
    a, b = range_input[0], range_input[1]
    x_i = x_i 
    y_i = y_i 

    X = []
    for x_subs in x_i:
        x_tmp = []
        for degree in range(len(x_i)):
            x_tmp.append(x_subs ** degree)
        X.append(x_tmp.copy())
    
    a_coeffician = np.linalg.solve(X, y_i) 
    x_range = np.linspace(a, b, 500)
    
    print(a_coeffician)
    y_origin = [f(x_subs) for x_subs in x_range]
    y_solve = []
    
    for i in range(len(x_range)):
        res = 0
        for j in range(len(a_coeffician)):
            res += a_coeffician[j] * x_range[i]**j
        y_solve.append(res)
            

    plt.title("f(x) = sin(9x) 20 points")

    plt.ylim(-6, 6)
    plt.plot(x_range, y_origin, label="origin")
    plt.plot(x_range, y_solve, label="interpole")
    # plt.plot(x_i, y_i, "ok", label="P(x) points")
    plt.legend()

def lagrange(range_input, x_i, y_i, m):
    a, b = range_input[0], range_input[1]
    x_i = x_i 
    y_i = y_i

    def L(index, x):
        numerator = 1
        decorater = 1 

        for i in range(m):
            if i == index: continue
            numerator *= x - x_i[i]

        for i in range(m):
            if i == index: continue
            decorater *= x_i[index] - x_i[i]

        return numerator/decorater 

    def P(x: int):
        result = 0
        for i in range(m):
            result += y_i[i] * L(i, x)
        
        return result
    
    x_range = np.linspace(a, b, 500)
    y_origin = [f(x_subs) for x_subs in x_range]
    y_solve = [P(x_subs) for x_subs in x_range]


    plt.ylim(-6, 6)
    # plt.plot(x_range, y_origin, label="origin")
    plt.plot(x_range, y_solve, "--", label="Lagrange")
    plt.plot(x_i, y_i, "ok", label="P(x) points")
    plt.legend()
    plt.savefig("./resultImages/Lagrange2.png")
    plt.show()
    

if __name__ == "__main__":
    range_data = (0, 4)
    M = 20
    range_input, x_i, y_i = generate_data(range_data, M)
    interpolate(range_data, x_i, y_i, M)
    lagrange(range_data, x_i, y_i, M)