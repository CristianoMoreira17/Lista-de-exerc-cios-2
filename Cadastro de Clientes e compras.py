quantidade_clientes = 0
soma_gastos = 0
maior_gasto = -1
cliente_que_mais_gastou = ""

while True:
    nome = input("Nome do cliente: ")
    valor = input("Valor total gasto (somente número inteiro): ")

    if not valor.isdigit():
        print("X Valor inválido. Digite apenas números inteiros.")
        continue

    valor = int(valor)
    quantidade_clientes += 1
    soma_gastos += valor

    if valor > maior_gasto:
        maior_gasto = valor
        cliente_que_mais_gastou = nome

    continuar = input("Deseja cadastrar outro cliente? (S/N): ").strip().upper()
    if continuar != "S":
        break

if quantidade_clientes > 0:
    print(f"\nTotal de clientes: {quantidade_clientes}")
    print(f"Soma total de gastos: R$ {soma_gastos:.2f}")
    print(f"Cliente que mais gastou: {cliente_que_mais_gastou} (R$ {maior_gasto:.2f})")
else:
    print("Nenhum cliente foi cadastrado.")
