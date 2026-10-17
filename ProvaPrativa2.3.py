quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_impares = 0
quantidade_total = 0
soma_total = 0
print("Digite {0} para sair da repetição:")
while True:
    numero = int(input("Digite um número: "))
    if numero==0:
        break
    quantidade_total=quantidade_total+1
    soma_total=soma_total+numero
    if numero%2==0:
        soma_pares=soma_pares+numero
        quantidade_pares=quantidade_pares+1
    else:
        soma_impares=soma_impares+numero
        quantidade_impares=quantidade_impares+1
if quantidade_pares > 0:
    media_pares =soma_pares / quantidade_pares
else:
    media_pares = 0
if quantidade_impares > 0:
    media_impares = soma_impares / quantidade_impares
else:
    media_impares = 0
print("Quantidade total de números:", quantidade_total)
print("Soma total dos números:", soma_total)
print("Média dos números pares:", media_pares)
print("Média dos números ímpares:", media_impares)