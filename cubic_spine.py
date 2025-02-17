import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import CubicSpline

def f(x: float) -> float:
    return 1.0/(1+25*x**2)
    
def generate_points(a, b, n):
    x_points = np.linspace(a, b, n)
    y_points = [f(x) for x in x_points]

    return x_points, y_points

if __name__ == "__main__":
    x_points, y_points = generate_points(-5, 5, 50)
    
    cs = CubicSpline(x_points, y_points, bc_type="natural")
    
    x_fine = np.linspace(-5, 5, 200)
    y_fine = cs(x_fine)
    
    
    plt.plot(x_points, y_points, 'o', label="Data Points")
    plt.plot(x_fine, [f(x) for x in x_fine], label="Origin")
    plt.plot(x_fine, y_fine, label="Cubic Spline")
    plt.legend()
    plt.show()