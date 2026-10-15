"""Calculadora básica con entrada y salida por consola."""

print("CALCULADORA BÁSICA")
try:
    numero_1 = float(input("Primer número: "))
    numero_2 = float(input("Segundo número: "))
except ValueError:
    print("Error: introduzca números válidos; use punto decimal.")
else:
    print(f"Suma: {numero_1 + numero_2:g}")
    print(f"Resta: {numero_1 - numero_2:g}")
    print(f"Multiplicación: {numero_1 * numero_2:g}")
    if numero_2 == 0:
        print("División: no se puede dividir entre cero.")
    else:
        print(f"División: {numero_1 / numero_2:g}")
