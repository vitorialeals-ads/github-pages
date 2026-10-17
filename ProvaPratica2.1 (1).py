ct=0
soma=0
maior_que_vinte=0
print("Digite {0} para sair da repetição")
while True:
    valor=float(input("Digite um número real:"))
    if valor==0:
        break
    ct=ct+1
    soma=soma+valor
    if valor>20:
        maior_que_vinte=maior_que_vinte+1
if ct>0:
    media=soma/ct
else:
    media=0
print("\nA quantidade de valores digitados é igual:", ct)
print("\nA soma dos valores digitados é igual:", soma)
print("\nA média aritmética é igual:", media)
print("\nA quantidade de valores maiores que 20 é igual:", maior_que_vinte)