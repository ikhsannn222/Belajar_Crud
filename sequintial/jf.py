# Soal no 2 (Problem set 3.4 No 11)
# Total pagar
P = 80

# perhitungan:
# 4x + y = 80 → y = 80 − 4x
# Luas A(x) = x(80 − 4x)
# Maksimum ketika x = 10

x = 10
y = P - 4*x
A = x * y

# OUTPUT
print("Dimensi,Nilai,Satuan")
print(f"Lebar Kandang: {x} kaki")
print(f"Panjang Total Kandang: {y} kaki")
print(f"Luas Maksimum Total: {A} ft^2")
# -----------------------------------------
# Tambahan: Grafik fungsi luas A(x)
# -----------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Domain x (nilai lebar kandang)
x_vals = np.linspace(0, P/4, 300)

# Fungsi luas
A_vals = x_vals * (P - 4 * x_vals)

# Plot grafik
plt.plot(x_vals, A_vals)
plt.title("Grafik Fungsi Luas A(x) = x(80 - 4x)")
plt.xlabel("Lebar x (kaki)")
plt.ylabel("Luas A(x) (ft²)")
plt.grid(True)

# Menandai titik maksimum
plt.scatter([x], [A], s=60)
plt.text(x, A, f"  Maksimum di x={x}, A={A}", verticalalignment='bottom')
plt.show()
