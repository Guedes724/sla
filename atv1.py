numeros = input("Digite uma lista de números : ").split()

numeros = [int(num) for num in numeros]

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))