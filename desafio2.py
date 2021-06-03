

lista = []
count = 0
n1 = int(input('Escreva o numero de matérias: ' ))
n2 = int(input('Digite o valor de cada nota de cada matéria: ')) 
quant = int(input("Digite a quantidade de matérias que deseja digitar: "))

media = n1 + n2 / 2
print('A média entre {} e {} é igual:{}'.format(n1, n2, media))


while quant != count:
    media = float(input("Digite um número: "))
        
    lista.append(media)
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))

