import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageSequence

def f(x: int) -> float:
    return x**2 - 4

def f_pi(x: int) -> float:
    return math.sin(x)

a = 0
b = 5 
count = 0
last_m = None

x_val = []
while (b - a) > 1e-15:
    m = a + (b - a) / 2
    x_val.append(m)

    if f(m) == 0:
        break
    elif f(a) * f(m) < 0:
        b = m
    if f(b) * f(m) < 0:
        a = m

    print(m)
    last_m = m
    count += 1
    
error = 1e-15
theory = math.log2(abs(b-a/error))

x = np.linspace(-5, 5, 200) 
y = [f(i) for i in x]

plt.xlim(-1, 5)
plt.ylim(-5, 5)
plt.axhline(0, color='black', lw=0.5)
plt.plot(x, y)

it = 15
for i in range(it):
    plt.plot(x_val[i], f(x_val[i]), 'ro')
    plt.savefig(f"./images/bisection_{i}.png")

frames = []
for i in range(15):
    img = Image.open(f"./images/bisection_{i}.png")
    frames.append(img)
    
frames[0].save("result.gif", save_all=True, append_images=frames[1:], loop=1, duration=1000)

print(f"Here is the last m: {m}")
print(f"This is the theory iteration approximate {theory}")
print(f"The actual number of iterations: {count}")
plt.show()


    