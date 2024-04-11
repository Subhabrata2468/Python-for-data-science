'''
Plot the Normal PDFs using various value of μ and σ as mentioned below:
μ  σ
0  1
0  2
0  0.5
-1 1
'''
import math
import matplotlib.pyplot as plt

# Define parameters: μ and σ values
parameters = [
    (0, 1),
    (0, 2),
    (0, 0.5),
    (-1, 1)
]

# Generate x values for plotting
x_values = [i / 10 for i in range(-50, 51)]  # Generate x values from -5 to 5 with step size 0.1

# Plot the Normal PDFs
plt.figure(figsize=(10, 6))
for mu, sigma in parameters:
    pdf_values = [1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) for x in x_values]
    plt.plot(x_values, pdf_values, label=f"μ={mu}, σ={sigma}")

plt.title('Normal Probability Density Functions')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
