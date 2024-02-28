import numpy as np
import matplotlib.pyplot as plt

# Grid-innstillinger
Nx, Ny = 120, 120
Lx, Ly = np.pi, np.pi
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)

# Initialiserer løsningsmatrisen
phi = np.zeros((Nx, Ny))

# Definerer kildefunksjonen for en kondensator
f = np.zeros((Nx, Ny))
plate_thickness = Nx//20  # Tykkelsen på platene (i gridpunkter)
plate_position = Ny//4  # Posisjonen til platene fra topp og bunn
for i in range(Nx//2 - plate_thickness//2, Nx//2 + plate_thickness//2):
    f[i, plate_position] = 100.0  # Positiv ladning på den ene platen
    f[i, Ny-plate_position] = -100.0  # Negativ ladning på den andre platen

# Simpel Poisson-løkke
for it in range(1000):
    phi_old = phi.copy()
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            phi[i, j] = 0.25 * (phi_old[i+1, j] + phi_old[i-1, j] + phi_old[i, j+1] + phi_old[i, j-1] - dx**2 * f[i, j])

# Viser løsningen som en 2D konturplot
plt.figure(figsize=(6, 5))
plt.contourf(x, y, phi, 100, cmap='cool')
plt.colorbar(label='$\phi$ - Potensial')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Elektrostatisk potensial i en kondensator')
plt.show()
