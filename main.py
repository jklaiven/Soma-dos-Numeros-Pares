inic = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o núero final do internvalo: "))

somaPares = 0

for numero in range(inic, fim + 1):
  if numero % 2 == 0:
    somaPares += numero

if somaPares > 0:
  print(f"A soma dos número no intervalo é: {somaPares}")
else:
  print("Não há númmeros pares no intervalor.")

  