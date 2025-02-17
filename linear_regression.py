import numpy as np
import matplotlib.pyplot as plt

def f(x: float) -> float:
    return 5 + 3 * x
    
def generate_points(a, b, m):
    x_points = np.random.uniform(a, b, m)
    y_points = f(x_points)
    y_points_noise = y_points + np.random.rand(m) - 0.5
    
    return x_points, y_points_noise
    
if __name__ == "__main__":
    m = 50
    # data_x, data_y = generate_points(-5, 5, m) 
    
    data_x = np.genfromtxt("./CSV/x_points.txt")
    data_y = np.genfromtxt("./CSV/y_points.txt")
    
    A = np.zeros((2, 2))
    b = np.zeros(2)
    
    A[0, 0] = m
    A[0, 1] = np.sum(data_x)
    A[1, 0] = np.sum(data_x)
    A[1, 1] = np.sum(data_x ** 2)
    
    b[0] = np.sum(data_y)
    b[1] = np.sum(data_x * data_y)
    
    c = np.linalg.solve(A, b)
    
    print(c[0], c[1])

    def F(x):
        return c[0] + c[1]*x
    
    x_fine = np.linspace(0, 10, 200)
    y_fine = F(x_fine)
    
    plt.plot(data_x, data_y, "o", label="data")
    plt.plot(x_fine, y_fine, label="Linear Regression")
    plt.show()