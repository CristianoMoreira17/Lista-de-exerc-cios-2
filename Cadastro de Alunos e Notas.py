quantidade_de_aluno = 0
soma_notas = 0
maior_nota = -1 
aluno_maior_nota = ""


while True:
    aluno = input("Qual o nome do aluno: ")
    
    notafinal = input("Qual a nota final: ")
    try:
        notafinal2 = float(notafinal)
    except ValueError:
        print("X Digite apenas números (inteiros ou com ponto).")
        continue

    quantidade_de_aluno += 1
    soma_notas += notafinal2

    if notafinal2 > maior_nota:
        maior_nota = notafinal2
        aluno_maior_nota = aluno


    continuar =  input("deseja continuar, S/N:" ).strip().upper()   
    if continuar != "S":
        break

if quantidade_de_aluno > 0:
    media = soma_notas / quantidade_de_aluno
    print(f"\nTotal de alunos: {quantidade_de_aluno}")
    print(f"Média da turma: {media:.2f}")
    print(f"Aluno com maior nota: {aluno_maior_nota} ({maior_nota})")
else:
    print("Nenhum aluno foi registrado.")