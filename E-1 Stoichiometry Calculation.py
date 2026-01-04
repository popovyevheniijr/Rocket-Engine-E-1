import numpy as np

# 1. Input data
# Empirical formula of kerosene RP-1 according to Dobrovolsky
C_atoms = 7.2107
H_atoms = 13.2936
# Given mass ratio of components (Oxidizer/Fuel)
Km = 2.29

# 2. Constants
# Precise molar masses of atoms, g/mol
M_C = 12.011
M_H = 1.008
M_O = 15.999

# 3. Stoichiometry calculation
# Calculate molar mass of the fuel molecule
M_fuel = C_atoms * M_C + H_atoms * M_H
# Calculate the required moles of oxygen (x) per 1 mol of fuel
# Reaction equation: C_nH_m + x*O2 -> a*CO2 + b*CO + c*H2O + d*H2
x = (Km * M_fuel) / (2 * M_O)

# 4. Solving the material balance system
# Coefficients y = [a, b, c, d]
# Construct matrix A for the linear system Ay = b
# Equations:
# 1. C:  a + b = C_atoms
# 2. H:  c + d = H_atoms / 2
# 3. O:  2a + b + c = 2x
# 4. Assumption: b = d  ->  b - d = 0
A = np.array([
    [1, 1, 0, 0],   # Carbon (C)
    [0, 0, 1, 1],   # Hydrogen (H)
    [2, 1, 1, 0],   # Oxygen (O)
    [0, 1, 0, -1]   # Simplifying assumption (b=d)
])

# Construct vector of right-hand sides b
b_vector = np.array([
    C_atoms,
    H_atoms / 2,
    2 * x,
    0
])

# Solve the linear system
coeffs = np.linalg.solve(A, b_vector)
a, b, c, d = coeffs  # Unpacking for convenience

# --- 5. AVERAGE MOLAR MASS CALCULATION ---
# Molar masses of combustion products, g/mol
M_CO2 = M_C + 2 * M_O
M_CO = M_C + M_O
M_H2O = 2 * M_H + M_O
M_H2 = 2 * M_H

# Total mass of products (numerator)
total_mass = a * M_CO2 + b * M_CO + c * M_H2O + d * M_H2
# Total moles of products (denominator)
total_moles = a + b + c + d

# Final average molar mass
M_avg = total_mass / total_moles

print(f"a (CO2): {a:.2f}")
print(f"b (CO):  {b:.2f}")
print(f"c (H2O): {c:.2f}")
print(f"d (H2):  {d:.2f}")
print(f"Average molar mass of combustion products: {M_avg:.2f} g/mol")