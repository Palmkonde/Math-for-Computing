import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 2 - 4

def f_prime(x):
    return 2 * x

def f_alpha(x: float) -> float:
    return (-1/3)*(x**2 - 4) + x

def find_root_newton(f, f_prime, x0, num_iter):
    x_vals = []
    it = 0
    for i in range(num_iter):
        x_vals.append(x0)
        x0 = x0 - f(x0) / f_prime(x0)
        it += 1
    return x0, it, x_vals


def find_root_bisect(f, a, b, num_iters):
    x_vals = []
    if f(a) * f(b) > 0:
        print("No root found")
        return 0,0,0
    else:
        it = 0
        while it < num_iters:
            c = (a + b) / 2
            x_vals.append(c)
            if f(c) == 0:
                return c, it
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
            it += 1
        return (a + b) / 2, it, x_vals

def find_root_fixedpoint(f, x0: float, num_iters: int):
    x_vals = []
    it = 0
    for _ in range(num_iters):
        x0 = f_alpha(x0)
        x_vals.append(x0)
        it += 1
    return x0, it, x_vals
        


a = 0
b = 3
eps = 0.00001
num_iter = 50
real_solution = 2

c, it, x_vals = find_root_newton(f, f_prime, 0.5, num_iter)
c1, it1, x_vals1 = find_root_bisect(f, a, b, num_iter)
c2, it2, x_vals2 = find_root_fixedpoint(f_alpha, 0.5, num_iter)



it_nums = [i for i in range(it)]
err_values = [abs(x - real_solution) for x in x_vals]
err_values1 = [abs(x - real_solution) for x in x_vals1]
err_values2 = [abs(x - real_solution) for x in x_vals2]

print(f"Root(Newton's method): {c} found in {it} iterations.")
print(f"Root(Bisection): {c1} found in {it1} iterations.")
print(f"Root(Fixed point): {c2} found in {it2} iterations.")

fig, ax = plt.subplots()
ax.plot(it_nums, err_values, label="Newton")
ax.plot(it_nums, err_values1, label="Bisect")
ax.plot(it_nums, err_values2, label="Fixed Root")
ax.set_yscale('log')
ax.set_title("Error on each step")
ax.set_xlabel("Iteration")
ax.set_ylabel("Error")
ax.legend()
plt.savefig("result.png")
plt.show()