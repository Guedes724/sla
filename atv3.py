# Solicita ao usuário para digitar um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    # Inicializa os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1

    # Exibe os n primeiros números da sequência
    print("Os primeiros", n, "números da sequência de Fibonacci são:")

    # Exibe os números da sequência
    for _ in range(n):
        print(a, end=" ")
        # Atualiza os valores de a e b para os próximos números
        a, b = b, a + b
