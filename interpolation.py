import numpy as np
import matplotlib.pyplot as plt

from typing import Tuple, List

def f(x: int) -> None:
    return np.sin(x) 

def interpolate(
        range_input: Tuple[int, int], 
        m: int) -> None:
    a, b = range_input[0], range_input[1]
    x_i = [np.random.uniform(a, b) for _ in range(m)]
    y_i = [f(x_subs) for x_subs in x_i]

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
            

    plt.ylim(-2, 2)
    plt.plot(x_range, y_origin, label="origin")
    plt.plot(x_range, y_solve, label="interpole")
    plt.legend()
    plt.show()
     

if __name__ == "__main__":
    interpolate((-30, 30), 100)