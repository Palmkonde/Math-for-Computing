def f(x:float) -> float:
    return (x**2) - 5*x + 4

def df(x: float) -> float:
    return 2*x - 5


def newton_method(func, d_func, start: float, max_iter=10000, epsilion=1e-10):
    prev_x = func(start)
    cnt = 0

    for _  in range(max_iter):
        x_nx = prev_x - func(prev_x)/d_func(prev_x)
        cnt += 1

        print(x_nx)
        if abs(x_nx - prev_x) < epsilion:
            break
            
        prev_x = x_nx
    
    print(f"Used iteration: {cnt}")

if __name__ == "__main__":
    newton_method(f, df, 6)