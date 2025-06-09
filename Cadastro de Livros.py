quantidade_livros = 0
quantidade_novos = 0
ano_mais_antigo = None
livro_mais_antigo = ""

while True:
    titulo = input("Título do livro: ")
    
    ano = input("Ano de publicação (maior que zero): ")
    if not ano.isdigit() or int(ano) <= 0:
        print("X Ano inválido. Digite um número inteiro maior que zero.")
        continue
    ano = int(ano)

    estado = input("Estado do livro (novo/usado): ").strip().lower()
    if estado not in ["novo", "usado"]:
        print("X Estado inválido. Digite apenas 'novo' ou 'usado'.")
        continue

    quantidade_livros += 1
    if estado == "novo":
        quantidade_novos += 1

    if ano_mais_antigo is None or ano < ano_mais_antigo:
        ano_mais_antigo = ano
        livro_mais_antigo = titulo

    continuar = input("Deseja cadastrar outro livro? (S/N): ").strip().upper()
    if continuar != "S":
        break

if quantidade_livros > 0:
    print(f"\nTotal de livros cadastrados: {quantidade_livros}")
    print(f"Total de livros novos: {quantidade_novos}")
    print(f"Livro mais antigo: '{livro_mais_antigo}' ({ano_mais_antigo})")
else:
    print("Nenhum livro foi cadastrado.")
