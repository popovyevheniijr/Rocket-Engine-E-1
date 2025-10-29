import math

# Calculation of molar mass (result of C_7.2H_13.29 + O_2)
M_aprox = ((32 * 7.2 + (13.29/2) * 18) / 14.5)/1000

# Input data
g = 1.2        # gamma - adiabatic index
R = 8.314      # R - universal gas constant (J / (mol * K))
M = round(M_aprox, 3)   # M - molar mass (kg / mol)
T_k = 3831     # T_k (t) - combustion chamber temperature (K)
pressure_ratio = 0.0338  # pressure ratio (p_a / p_k)

# Calculations by formulas
# Calculate the exponent
exponent = (g - 1) / g

# Calculate V_a
term1 = (2 * g * R * T_k) / ((g - 1) * M)
term2 = (1 - math.pow(pressure_ratio, exponent))
V_a = math.sqrt(term1 * term2)

print(f"\nExhaust velocity (V_a or I_sp): {V_a:.2f} m/s")

# 2. Calculation of mass flow rate per second (m_sec)
P_thrust = 3000.0 # assumed thrust (N)
m_sec = P_thrust / V_a
print(f"Mass flow rate (m_sec) for P={P_thrust} N: {m_sec:.4f} kg/s")

# 3. Calculation of specific impulse in seconds (I_sp)
g_0 = 9.81 # gravitational acceleration (m/s^2)
I_sp = V_a / g_0
print(f"Specific impulse (I_sp): {I_sp:.2f} s")

# 5. Calculation of geometric expansion ratio of the nozzle (F_a / F_crit)
num = (2.0/(g+1.0))**(1.0/(g-1.0)) * math.sqrt((g-1.0)/(g+1.0))
den = pressure_ratio**(1.0/g) * math.sqrt(1.0 - pressure_ratio**((g-1.0)/g))
F_a = num / den
print("Geometric expansion ratio of the nozzle (F_a):", F_a)
