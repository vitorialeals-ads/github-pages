ct=0
soma=0
numero= int(input("Digite o primeiro valor:"))
for valor in range(numero,-1,-1):
    print(valor)
    ct=ct+1
    soma=soma+valor
print("Quantidade de valores da sequência:",ct)
print("Soma dos valores da sequência:", soma)