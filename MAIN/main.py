import json
import os

def main():
    if not os.path.exists("veiculos.json"):
        with open("veiculos.json", "w") as f:
            f.write("[]")  # Write an empty list to the file

def cadastrar_veiculo():
    modelo = input("Informe o modelo do veículo: ")
    ano = int(input("Informe o ano do veículo: "))
    cor = input("Informe a cor do veículo: ")
    acessorios = {}
    acessorios["ar"] = input("O veículo possui ar condicionado? (S/N): ").upper() == "S"
    acessorios["vidro-eletrico"] = input("O veículo possui vidros elétricos? (S/N): ").upper() == "S"
    acessorios["direcao"] = input("O veículo possui direção hidráulica? (S/N): ").upper() == "S"
    return {
        "modelo": modelo,
        "ano": ano,
        "cor": cor,
        "acessorios": acessorios,
        "alugueis": []  # Inicializa a lista de aluguéis como vazia
    }

def cadastrar_aluguel(veiculo):
    while True:
        cliente = input("Informe o nome do cliente (ou deixe em branco para encerrar): ")
        if not cliente:
            break  # Sai do loop se o nome do cliente estiver em branco
        valor = float(input("Informe o valor do aluguel: "))
        quilometragem = int(input("Informe a quilometragem do aluguel: "))
        aluguel = {
            "cliente": cliente,
            "valor": valor,
            "quilometragem": quilometragem
        }
        veiculo["alugueis"].append(aluguel)

def ler_veiculos():
    with open("veiculos.json", "r") as f:
        dados = json.load(f)
    return dados

def escrever_veiculos(dados):
    with open("veiculos.json", "w") as f:
        json.dump(dados, f, indent=2)  # Adiciona indentação para melhor legibilidade

if __name__ == "__main__":
    main()

    # Lê os veículos cadastrados
    veiculos = ler_veiculos()

    # Cadastra um novo veículo
    veiculo = cadastrar_veiculo()
    veiculos.append(veiculo)

    # Cadastra aluguéis para o veículo
    cadastrar_aluguel(veiculo)

    # Escreve os veículos cadastrados
    escrever_veiculos(veiculos)