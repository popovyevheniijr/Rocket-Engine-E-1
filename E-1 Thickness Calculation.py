import math

def thickness(P, R, alpha=None, sigma_B=500e6, safety_factor=2):
    if alpha is None:  # Cylindrical part
        print("Cylindrical part calculation:")
        N_theta = P * R
        N_m = P * R / 2
    else:  # Conical part
        print("Conical part calculation:")
        alpha_rad = math.radians(alpha)
        N_m = (P * R) / (2 * math.sin(alpha_rad)**2)
        N_theta = (P * R) / math.sin(alpha_rad)

    # Calculation of approximate wall thickness
    delta = (safety_factor * math.sqrt(N_m**2 + N_theta**2 - N_m * N_theta)) / sigma_B
    return delta

# Input data
p = 3e6 # p_1 - pressure in Injector and Nozzle Inlet (Pa)
p_3 = 1e6 # p_3 - approximate pressure in Nozzle Exit (Pa)
R_1 = 59/1000 # R_1 - radius of Injector (m)
R_2 = 59/1000 # R_2 - radius of Nozzle Inlet (m)
R_3 = 34/1000 # R_3 - radius of Nozzle Exit (m)
a_2 = 30 # b -  converging half-angle (deg)
a_3 = 20 # Tn - throat-to-exit angle (deg)
sigma = 700e6  # sigma_B - Tensile Strength of Inconel (Pa)

# Calculation for cylindrical part 1
thickness_1 = thickness(p, R_1, sigma_B=sigma)
print(f"Wall thickness of cylindrical part: {thickness_1 * 1000} mm\n")

# Calculation for conical part 2
thickness_2 = thickness(p, R_2, a_2, sigma_B=sigma)
print(f"Wall thickness of Nozzle inl: {thickness_2 * 1000:.2f} mm\n")

# Calculation for conical part 3
thickness_3 = thickness(p_3, R_3, a_3, sigma_B=sigma)
print(f"Wall thickness of Nozzle exi: {thickness_3 * 1000:.2f} mm\n")