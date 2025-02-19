import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Circle

RANGE = (-5, 5)

def generate_points(num_points):
    x_answer, y_answer = -3, 2
    xy_points = np.random.uniform(RANGE[0], RANGE[1], size=(num_points, 2))

    return (x_answer, y_answer), xy_points

if __name__ == "__main__":
    xy_answer, xy_points = generate_points(6)

    d = np.array([np.linalg.norm(xy - xy_answer) - np.random.uniform(-0.5, 0.5) for xy in xy_points])

    x_0, y_0 = xy_points[0]
    A = np.zeros((len(d) - 1, 2))
    b = np.zeros(len(d) - 1)
    
    for i in range(0, len(d) - 1):
        x_i, y_i = xy_points[i + 1]
        
        b[i] = d[i + 1]**2 - d[0]**2 + x_0**2 + y_0**2 - x_i**2 - y_i**2

        for j in range(2): 
            if j == 0:
                A[i, j] = 2*x_0 - 2*x_i 
            else: 
                A[i, j] = 2*y_0 - 2*y_i 
                
    
    c = np.linalg.solve(A.T@A, A.T@b)
    print(c)
        
    plt.plot(xy_points[:, 0], xy_points[:, 1], 'o', label="Data points")
    plt.plot(xy_answer[0], xy_answer[1], 'x', label="Exact Answer")
    plt.plot(c[0], c[1], '^', label="Approximate")
    plt.legend()
    plt.show()


    