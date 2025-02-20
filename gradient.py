import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def f_prime(x):
    return 2*x

def multivariate_gradient():

    def get_df_value(vector: list[float, float]) -> list[float, float]:
        x, y = vector
        return [2*(x-2), 4*(y-3)]

    # initial variable
    xy_0 = [12, 12]  # x, y
    alpha = 0.01

    xy_prev = [0, 0]
    xy_next = xy_0
    eps = 0.01

    while True:
        xy_prev = xy_next.copy()

        xy_next[0] = xy_prev[0] - alpha*get_df_value(xy_prev)[0]
        xy_next[1] = xy_prev[1] - alpha*get_df_value(xy_prev)[1]
        
        if(np.linalg.norm(xy_prev - xy_next) < eps):
            break

        print(f"{xy_next[0]} {xy_next[1]}")

    print(f"minimum value at point {xy_next[0]} {xy_next[1]}")

if __name__ == "__main__":
    multivariate_gradient()