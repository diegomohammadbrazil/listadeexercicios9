
         
         
n_pessoas = int(input("Digite o número de pessoas que ira digitar a idade: "))
lista = []

for i in range(n_pessoas):
    idade = lista.append(int(input("Digite a idade: ")))
for i in range(n_pessoas):
    est_civil = lista.append(int(input("Digite seu estado civil: [1] Solteito, [2] Casado, [3] separados: ")))    


if sum(lista) / len(lista) < 15:
    print("solteiro")
elif sum(lista) / len(lista) >= 15 and sum(lista) / len(lista) < 15:
    print("casados")
else:
    print("separados")