ct=0
soma=0
aprovados=0
reprovados=0
print("Digite {-1} para sair da repetição:")
while True:
    nota = float(input("Digite a nota do aluno: "))
    if nota==-1:
        break
    ct=ct+1
    soma=soma+nota
    if nota >= 5:
      aprovados=aprovados+1
    else:
      reprovados=reprovados+1
if ct> 0:
    media_turma=soma/ct
print(f"\nA quantidade de alunos que fizeram a prova é igual:", ct)
print(f"\nA quantidade de alunos aprovados é igual:", aprovados)
print(f"\nA quantidade de alunos reprovados é igual:", reprovados)
print(f"\nA média da turma é igual : {media_turma:.2f}")
