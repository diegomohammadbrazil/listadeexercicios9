#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

n1 = int(input("\nDigite o número: "))
n2 = int(input("Digite o número: "))
n3 = int(input("Digite o número: "))
n4 = int(input("Digite o número: "))
n5 = int(input("Digite o número: "))
n6 = int(input("Digite o número: "))
n7 = int(input("Digite o número: "))
n8 = int(input("Digite o número: "))
n9 = int(input("Digite o número: "))
n10 = int(input("Digite o número: "))
n11 = int(input("Digite o número: "))
n12 = int(input("Digite o número: "))
n13 = int(input("Digite o número: "))
n14 = int(input("Digite o número: "))
n15 = int(input("Digite o número: "))
n16 = int(input("Digite o número: "))
n17 = int(input("Digite o número: "))
n18 = int(input("Digite o número: "))
n19 = int(input("Digite o número: "))
n20 = int(input("Digite o número: "))
list1 = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20]

par = 0
impar = 0

for value in list1:
    if value % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print("Par: ", par, "\nImpar: ", impar)