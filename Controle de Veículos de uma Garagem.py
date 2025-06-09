quantidade_veiculos = 0
soma_dias = 0
maior_tempo = -1
veiculo_mais_tempo = ""

while True:
    modelo = input("Modelo do veículo: ")
    dias = input("Número de dias que ficará na garagem: ")

    if not dias.isdigit():
        print("X Digite apenas números inteiros para os dias.")
        continue

    dias = int(dias)
    quantidade_veiculos += 1
    soma_dias += dias

    if dias > maior_tempo:
        maior_tempo = dias
        veiculo_mais_tempo = modelo

    continuar = input("Deseja cadastrar outro veículo? (S/N): ").strip().upper()
    if continuar != "S":
        break

if quantidade_veiculos > 0:
    media = soma_dias / quantidade_veiculos
    print(f"\nTotal de veículos: {quantidade_veiculos}")
    print(f"Média de dias: {media:.2f}")
    print(f"Veículo que ficará mais tempo: {veiculo_mais_tempo} ({maior_tempo} dias)")
else:
    print("Nenhum veículo foi cadastrado.")
