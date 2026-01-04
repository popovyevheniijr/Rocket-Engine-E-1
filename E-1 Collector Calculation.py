import math

# 1. Input data
safety_factor = 1.2         # Safety margin for wall thickness (not used in hydro, but good to have)
a_mm = 0.9                    # Channel width (mm) - Optimized for SLM
b_mm = 1.2                    # Channel height/depth (mm) - Optimized for heat transfer
k_roughness = 50e-6         # Roughness for SLM printing (m)
L_jacket = (190.84 + 77) / 1000  # Total length of the cooling tract (m)
N_channels = 70             # Number of channels
rho_cold = 780.0            # Density at inlet (kg/m3)
mu_cold = 1.5e-3            # Viscosity at inlet (Pa*s)
rho_hot = 700.0             # Density drops due to heating (kg/m3)
m_total = 0.3 * 1.18        # Total mass flow rate (kg/s)
K_loss_ratio = 0.1          # Manifold dP should be 10% of Channel dP

# 2. Cooling channels calculation
# Geometric conversion to SI
a = a_mm / 1000.0
b = b_mm / 1000.0
F_channel = a * b
D_hyd = 2 * F_channel / (a + b)

# Flow velocity in channels
v_channel = m_total / (rho_cold * F_channel * N_channels)

# Reynolds Number
Re = (rho_cold * v_channel * D_hyd) / mu_cold

print(f"Channel Velocity: {v_channel:.2f} m/s")
print(f"Reynolds Number:  {Re:.0f}")

# Friction Coefficient (Darcy-Weisbach) via Altshul formula
if Re > 2300:
    # Turbulent flow
    lam = 0.11 * ((k_roughness / D_hyd) + (68 / Re)) ** 0.25
    print("Flow Regime:TURBULENT")
else:
    # Laminar flow
    lam = 64 / Re
    print("Flow Regime: LAMINAR")

# Pressure Drop in Channels (Delta P_ch)
# Darcy formula: dP = lambda * (L/D) * (rho * v^2 / 2)
ksi_channel = lam * (L_jacket / D_hyd)
delta_p_ch = ksi_channel * (rho_cold * v_channel**2) / 2

print(f"Channel Pressure Drop: {delta_p_ch:.0f} Pa ({delta_p_ch/100000:.2f} bar)")


# 3. Inlet manifold (Cold RP-1)
# Allowable pressure drop in manifold (10% rule)
delta_p_inlet = delta_p_ch * K_loss_ratio

# Max allowed velocity in manifold (Bernoulli approximation)
v_max_inlet = math.sqrt(2 * delta_p_inlet / rho_cold)
print(f"Max Velocity:     {v_max_inlet:.2f} m/s")

# Required Area Calculation
F_inlet_required = safety_factor*(m_total / (2 * (rho_cold * v_max_inlet)))

print(f"Required Area:    {F_inlet_required * 1e6:.2f} mm2")

# Equivalent Diameter (Teardrop approx)
D_inlet_eq = 2 * math.sqrt(F_inlet_required / math.pi)
print(f"Equiv. Diameter:  {D_inlet_eq * 1000:.2f} mm")


# 4. Outlet manifold (Hot RP-1)
# Max allowed velocity (Hot) - dP is the same constraint (or slightly lower to be safe)
v_max_outlet = math.sqrt(2 * delta_p_inlet / rho_hot)
print(f"Max Velocity:     {v_max_outlet:.2f} m/s")

# Required Area Calculation (Hot)
F_outlet_required = safety_factor * (m_total / (2 * (rho_hot * v_max_outlet)))

print(f"Required Area:    {F_outlet_required * 1e6:.2f} mm2")

# Equivalent Diameter
D_outlet_eq = 2 * math.sqrt(F_outlet_required / math.pi)
print(f"Equiv. Diameter:  {D_outlet_eq * 1000:.2f} mm")


