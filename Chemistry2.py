import numpy as np
from scipy.integrate import solve_ivp

# Define the reaction rate function
def reaction_rate(t, y, k):
    A, B = y
    dAdt = -k * A
    dBdt = k * A
    return [dAdt, dBdt]

# Define the initial concentrations of the reactants
y0 = [1.0, 0.0]

# Define the reaction rate constant
k = 0.5

# Solve the differential equations using the ODE solver from SciPy
sol = solve_ivp(lambda t, y: reaction_rate(t, y, k), [0, 10], y0)

# Extract the time and solution arrays
t = sol.t
A = sol.y[0]
B = sol.y[1]

# Plot the results
import matplotlib.pyplot as plt
plt.plot(t, A, label='A')
plt.plot(t, B, label='B')
plt.xlabel('Time (s)')
plt.ylabel('Concentration (mol/L)')
plt.legend()
plt.show()
