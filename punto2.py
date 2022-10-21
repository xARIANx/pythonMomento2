def compararNumeros(num1, num2): return 1 if num1 > num2 else -1


total = compararNumeros(1, 10)


def resultado(): return print("El primer número es mayor que el segundo") if total == 1 else print(
    "El segundo número es mayor que el primero")


resultado()