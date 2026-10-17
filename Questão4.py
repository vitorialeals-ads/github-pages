valor1 = float(input("Digite o primeiro número:"))
valor2 = float(input("Digite o segundo número:"))
print("\nEscolha a operação:")
print("+ - Adição")
print("- - Subtração")
print("* - Multiplicação")
print("/ - Divisão")
operacao = input("Digite a operação desejada: ")
if operacao == "+":
    resultado = valor1+valor2
    print("\nResultado:", resultado)
elif operacao == "-":
    resultado = valor1-valor2
    print("\nResultado:", resultado)
elif operacao == "*":
    resultado = valor1*valor2
    print("\nResultado:", resultado)
elif operacao == "/":
    if valor2!= 0:
        resultado = valor1/valor2
        print("\nResultado:", resultado)
    else:
        print("\nNão é possível dividir por zero!")
else:
    print("\nOperação inválida!")