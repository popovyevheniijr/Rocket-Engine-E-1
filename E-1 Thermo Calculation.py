import math

# 1. Input data
g = 1.13              # gamma - adiabatic index
R = 8.314             # universal gas constant (J/(mol*K))
M = 23.74e-3          # molar mass (kg/mol)
T_k = 3475            # combustion chamber temperature (K)
g_0 = 9.81            # gravitational acceleration (m/s^2)
p_k = 3e6             # chamber pressure (Pa)
p_a = 0.8 * 101325          # ambient pressure at sea level (Pa)
p_H = 101325    # ambient pressure at ~20 km altitude (Pa)
pressure_ratio = p_a / p_k  # pressure ratio (p_a / p_k)

exponent = (g + 1) / (g - 1)
A_gamma = math.sqrt(g * (2 / (g + 1)) ** exponent)

# 2. Exhaust velocity calculation
exponent = (g - 1) / g
term1 = (2 * g * R * T_k) / ((g - 1) * M)
term2 = (1 - math.pow(pressure_ratio, exponent))
V_a = math.sqrt(term1 * term2)

# 3. Nozzle geometric expansion ratio (F_a / F_crit)
num = (2.0 / (g + 1.0)) ** (1.0 / (g - 1.0)) * math.sqrt((g - 1.0) / (g + 1.0))
den = pressure_ratio ** (1.0 / g) * math.sqrt(1.0 - pressure_ratio ** ((g - 1.0) / g))
F_a = num / den

# 4. Mass flow rate calculation from thrust
P_thrust = 3000.0  # assumed thrust (N)
gas_term = math.sqrt((R * T_k) / M)
term = ((p_a - p_H) / p_k) * F_a * (gas_term / A_gamma)
m_sec = P_thrust / (V_a + term)

# 5. Specific impulse at given ambient pressure
I_sp = P_thrust / (m_sec * g_0)

# 6. Throat area calculation
num = R * T_k / M
F_t = (m_sec * gas_term) / (p_k * A_gamma) * 1e6  # throat area in mm^2
r_t = math.sqrt(F_t / math.pi)  # throat radius in mm

# 7. Nozzle cut area calculation
F_A = F_a * F_t # Nozzle cut area in mm^2
r_a = math.sqrt(F_A / math.pi)  # Nozzle cut radius in mm


print(f"Exhaust velocity (w_a): {V_a:.2f} m/s")
print(f"Nozzle geometric expansion ratio (F_a): {F_a:.2f}")
print(f"Mass flow rate (m_sec) for P = {P_thrust} N: {m_sec:.4f} kg/s")
print(f"Specific impulse  (I_sp): {I_sp:.2f} s")
print(f"Throat area (F_t): {F_t:.4f} mm^2")
print(f"Throat diameter (D_t): {2*r_t:.4f} mm")
print(f"Nozzle cut area (F_A): {F_A:.4f} mm^2")
print(f"Nozzle cut diameter (D_A): {2*r_a:.4f} mm")