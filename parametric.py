import numpy as np
import matplotlib.pyplot as plt

from skimage import io, color, filters

def draw_circle(r: float):
    def x(t):
        return r * np.cos(t)

    def y(t):
        return r * np.sin(t)

    t_range = np.linspace(0, 2 * np.pi, 200)
    x_circle = x(t_range)
    y_circle = y(t_range)

    plt.figure(figsize=(8, 8))
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.plot(x_circle, y_circle)


def draw_heart(float):
    t_range = np.linspace(0, 2 * np.pi, 200)

    def x(t):
        return 16*np.pow(np.sin(t), 3)

    def y(t):
        return 13*np.cos(t)-5*np.cos(2 * t) - 2*np.cos(3*t) - np.cos(4*t)

    plt.figure(figsize=(8, 8))
    plt.plot(x(t_range), y(t_range))
    plt.show()


def generate_points(a: int, b: int, n: int, f, f2):
    t_range = np.linspace(a, b, n)

    x_range = f(t_range)
    y_range = f2(t_range)

    return x_range, y_range


def interpolate(range_input, x_i, y_i) -> None:
    a, b = range_input[0], range_input[1]
    x_i = x_i
    y_i = y_i

    X = []
    for x_subs in x_i:
        x_tmp = []
        for degree in range(len(x_i)):
            x_tmp.append(x_subs ** degree)
        X.append(x_tmp.copy())

    a_coeffician = np.linalg.solve(X, y_i)
    x_range = np.linspace(a, b, 500)

    y_solve = []

    # P(x)
    for i in range(len(x_range)):
        res = 0
        for j in range(len(a_coeffician)):
            res += a_coeffician[j] * x_range[i]**j
        y_solve.append(res)
        
    return y_solve

def interpolate_parametric():
    def f1(t):
        return 16*np.pow(np.sin(t), 3)

    def f2(t):
        return 13*np.cos(t)-5*np.cos(2 * t) - 2*np.cos(3*t) - np.cos(4*t)

    n = 10  # Number of points
    a, b = 0, 2 * np.pi  # Interval for parameter t
    t_values = np.linspace(a, b, n)  # Generate t values

    x_values = f1(t_values)
    y_values = f2(t_values)

    coeff_x = np.polyfit(t_values, x_values, n-1)
    coeff_y = np.polyfit(t_values, y_values, n-1)

    poly_x = np.poly1d(coeff_x)
    poly_y = np.poly1d(coeff_y)

    t_fine = np.linspace(a, b, 100)
    x_interp = poly_x(t_fine)
    y_interp = poly_y(t_fine)

    # Plot the results
    plt.figure(figsize=(8, 8))
    plt.plot(x_values, y_values, 'ro', label='Sample Points')
    plt.plot(x_interp, y_interp, 'b-', label='Polynomial Interpolation')
    plt.plot(f1(t_fine), f2(t_fine), 'g--', label='Actual Graph')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Parametric Interpolation of a Heart')
    plt.axis('equal')
    plt.grid()
    plt.show()
    
def gadient():

    # 1. Load the image
    image = io.imread("./images/Heart.jpeg")  # Replace with your image filename

    # 2. Convert to grayscale
    #    If there's an alpha channel, take only the first 3 channels (RGB).
    if image.shape[-1] == 4:
        image = image[..., :3]  # discard alpha
    gray = color.rgb2gray(image)

    # 3. Apply Sobel filter to get gradient magnitude
    edge_sobel = filters.sobel(gray)

    # 4. Threshold the gradient magnitude to isolate edges
    #    Adjust threshold as needed based on your image.
    threshold = 0.2
    edges = edge_sobel > threshold

    # 5. Extract the coordinates of the edge points
    edge_points = np.column_stack(np.nonzero(edges))

    # 6. Display results
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    axes[0].imshow(image)
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    axes[1].imshow(edge_sobel, cmap='gray')
    axes[1].set_title("Sobel Gradient Magnitude")
    axes[1].axis("off")

    axes[2].imshow(edges, cmap='gray')
    axes[2].set_title("Thresholded Edges")
    axes[2].axis("off")

    plt.tight_layout()
    plt.show()

    print("Number of edge points detected:", len(edge_points))

if __name__ == "__main__":
    gadient()    