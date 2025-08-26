def karatsuba(x, y):
    """
    Implementa o verdadeiro algoritmo de Karatsuba, que usa 3 chamadas recursivas.
    """
    # Caso base da recursão. Para números pequenos, a multiplicação direta é mais rápida.
    if x < 10 or y < 10:
        return x * y

    # Calcula o número de dígitos 'n' e o ponto de divisão 'q'.
    s_x, s_y = str(x), str(y)
    n = max(len(s_x), len(s_y))
    q = n // 2

    # Divide os números em partes inferiores e superiores.
    potencia_10 = 10 ** q
    A, B = divmod(x, potencia_10)
    C, D = divmod(y, potencia_10)

    # Produto das partes superiores
    z2 = karatsuba(A, C)

    # Produto das partes inferiores
    z0 = karatsuba(B, D)

    # z1 = (A+B)*(C+D) - z2 - z0
    produto_somas = karatsuba(A + B, C + D)
    z1 = produto_somas - z2 - z0

    # Resultado = z2 * 10^(2q) + z1 * 10^q + z0
    resultado = (z2 * 10 ** (2 * q)) + (z1 * 10 ** q) + z0

    return resultado


# Exemplo de uso
num1 = 12345678
num2 = 87654321
print(f"\nResultado do algoritmo de Karatsuba: {karatsuba(num1, num2)}")
print(f"Resultado da multiplicação normal:   {num1 * num2}")