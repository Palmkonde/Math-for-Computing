import numpy as np
import matplotlib.pyplot as plt

from typing import List, Union, Callable

def g(c: List[float], x:Union[int, float], f: List[Callable[[float], float]]):
    res = 0
    for i, func in enumerate(f):
        res += c[i] * func(x)
    
    return res
        
def generate_points(a: int, b: int, m: int, f: Callable[[float], float]):
    x_points = np.linspace(a, b, m)
    y_points = f(x_points)
    
    return x_points, y_points

if __name__ == "__main__":
    A_RANGE, B_RANGE = 10, 20
    # x_points, y_points = generate_points(A_RANGE, B_RANGE, 5, lambda x: np.sin(x))  
    
    data = np.genfromtxt('./CSV/data.csv', delimiter=',')
    x_points = data[:, 0]
    y_points = data[:, 1]
    
    A_RANGE = min(x_points)
    B_RANGE = max(x_points)

    list_func = [
        lambda x: x*0 + 1,
        lambda x: np.cos(x),
        lambda x: np.sin(x),
        lambda x: x,
        lambda x: x**2,
        lambda x: np.log(x)
    ]
    
    A = np.zeros((len(x_points), len(list_func)))
    b = np.zeros(len(y_points))
    
    for i in range(len(x_points)):
        for j in range(len(list_func)):
            A[i, j] = list_func[j](x_points[i])
    
    for i in range(len(y_points)):
        b[i] = y_points[i]

    c = np.linalg.solve(A.T@A, A.T@b) 
    
    for i in range(len(c)):
        print(f"C_{i}: {np.round(c[i])}")
    
    x_fine = np.linspace(A_RANGE, B_RANGE, 200)
    y_fine = g(c, x_fine, list_func)
    
    plt.plot(x_fine, y_fine, label="Approximate", zorder=3)
    plt.plot(x_points, y_points, 'o', label="Data points")
    plt.legend()
    plt.show()