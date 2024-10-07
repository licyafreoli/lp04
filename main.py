inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

soma_pares = 0
encontrou_pares = False

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero
        encontrou_pares = True

if encontrou_pares:
    print(f"A soma dos números pares no intervalo de {inicio} a {fim} é {soma_pares}.")
else:
    print("Não há números pares no intervalo.")
