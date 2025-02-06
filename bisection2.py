import matplotlib.pyplot as plt
import numpy as np
def f(x: int) -> float:
    return x**4 + 3*(x**3) + (x**2) - (2*x) - 0.5

x_val = []
def bisection(start: float, end: float) -> float:
    global x_val
    a = start
    b = end
    epsilon = 1e-10 
    m = None

    while abs(b - a) >= epsilon:
        m = (a + b) / 2
        x_val.append(m)
        f_m = f(m)
        f_a = f(a)
        if f_m == 0:
            break
        elif f_a * f_m < 0:
            b = m
        else:
            a = m
    return m 
    
def many_intervals(start: float, end: float, root = set()) -> set:
    midpoint = (start + end) / 2
    epsilon = 1e-2
    answer = root
    
    if f(start) * f(end) >= 0 and (end - start) > epsilon:
        answer = answer | (many_intervals(start, midpoint, answer))
        answer = answer | (many_intervals(midpoint, end, answer))
    else:
        answer = answer | {(bisection(start, end))}
    
    # print(answer)
    return answer

if __name__ == "__main__":
    start = -3
    end = 1

    x = np.linspace(-5, 5, 200) 
    y = [f(i) for i in x]
    
    print(many_intervals(start, end))
    plt.xlim(-5, 5)
    plt.ylim(-3, 3)
    plt.axhline(0, color='black', lw=0.5)
    plt.plot(x, y)
    
    for i in range(len(x_val)):
        plt.plot(x_val[i], f(x_val[i]), 'ro')
        plt.savefig(f"./images/bisection_{i}.png")
    plt.show()
