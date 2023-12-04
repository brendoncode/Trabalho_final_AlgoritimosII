import json
import os


def main():
    if not os.path.exists("main.json"):
        with open("main.json", "w") as f:
            f.write("[]")  # Write an empty list to the file


def menu():
    escolha = int(input("Escolha uma das opções abaixo: \n"
                        "1 - Cadastrar veículo \n"
                        "2 - Cadastrar aluguel \n"
                        "3 - Visualizar Alugueis \n"
                        "4 - Visualizar veículos \n"
                        "0 - Sair \n"
                        ": "))
    return escolha


def carros_disponiveis(veiculos):
    disponiveis = [i for i, veiculo in enumerate(veiculos) if not veiculo["alugueis"]]
    return disponiveis


def cadastrar_veiculo():
    modelo = input("Informe o modelo do veículo: ")
    ano = int(input("Informe o ano do veículo: "))
    cor = input("Informe a cor do veículo: ")
    acessorios = {}
    acessorios["ar"] = input("O veículo possui ar condicionado? (S/N): ").upper() == "S"
    acessorios["vidro-eletrico"] = input("O veículo possui vidros elétricos? (S/N): ").upper() == "S"
    acessorios["direcao"] = input("O veículo possui direção elétrica? (S/N): ").upper() == "S"
    return {
        "modelo": modelo,
        "ano": ano,
        "cor": cor,
        "acessorios": acessorios,
        "alugueis": []  # Inicializa a lista de aluguéis como vazia
    }


def cadastrar_aluguel(veiculos):
    disponiveis = carros_disponiveis(veiculos)

    if not disponiveis:
        print("Não há veículos disponíveis para aluguel.")
        return

    print("Veículos disponíveis para aluguel:")
    for i in disponiveis:
        print(f"{i} - {veiculos[i]['modelo']} {veiculos[i]['cor']}")

    while True:
        indice_veiculo = int(input("Informe o índice do veículo para alugar: "))
        if indice_veiculo not in disponiveis:
            confirmacao = input("Este veículo já está alugado. Deseja confirmar o aluguel? (S/N): ").upper()
            if confirmacao != "S":
                return

        veiculo = veiculos[indice_veiculo]
        cliente = input("Informe o nome do cliente (ou deixe em branco para encerrar): ")
        if not cliente:
            return  # Sai da função se o nome do cliente estiver em branco

        valor = float(input("Informe o valor do aluguel: "))
        quilometragem = int(input("Informe a quilometragem do aluguel: "))
        aluguel = {
            "cliente": cliente,
            "valor": valor,
            "quilometragem": quilometragem
        }
        veiculo["alugueis"].append(aluguel)
        print(f"Veículo {veiculo['modelo']} {veiculo['cor']} alugado para {cliente}.")
        break


def ler_veiculos():
    with open("main.json", "r") as f:
        dados = json.load(f)
    return dados


def escrever_veiculos(dados):
    with open("main.json", "w") as f:
        json.dump(dados, f, indent=2)  # Adiciona indentação para melhor legibilidade


def visualizar_alugueis(veiculos):
    if len(veiculos) == 0:
        print("Não há veículos cadastrados.")
        return

    print("Veículos com alugueis:")
    for i, veiculo in enumerate(veiculos):
        if veiculo["alugueis"]:
            print(f"{i} - {veiculo['modelo']} {veiculo['cor']} Alugado para {veiculo['alugueis'][-1]['cliente']}")

    indice_veiculo = int(input("Informe o índice do veículo para detalhes do aluguel (ou -1 para sair): "))
    if indice_veiculo == -1:
        return

    veiculo = veiculos[indice_veiculo]
    if not veiculo["alugueis"]:
        print("Veículo não possui alugueis.")
        return

    aluguel = veiculo["alugueis"][-1]
    total_a_pagar = aluguel["quilometragem"] * aluguel["valor"]

    print(f"\nDetalhes do aluguel:")
    print(f"Cliente: {aluguel['cliente']}")
    print(f"Valor do aluguel por KM: R${aluguel['valor']}")
    print(f"Quilometragem: {aluguel['quilometragem']} KM")
    print(f"Total a pagar: R${total_a_pagar}")

    # Adicionando submenu
    while True:
        submenu_escolha = int(input("Submenu Visualizar Alugueis: \n"
                                    "1 - Visualizar detalhes \n"
                                    "2 - Voltar ao menu principal \n"
                                    ": "))

        if submenu_escolha == 1:
            indice_aluguel = int(input("Informe o índice do aluguel para visualizar detalhes: "))
            if 0 <= indice_aluguel < len(veiculo["alugueis"]):
                detalhes_aluguel(veiculo["alugueis"][indice_aluguel], veiculo)
            else:
                print("Índice de aluguel inválido. Tente novamente.")
        elif submenu_escolha == 2:
            break
        else:
            print("Opção inválida. Tente novamente.")


def detalhes_aluguel(aluguel, veiculo):
    acessorios = veiculo["acessorios"]

    print("\nDetalhes do aluguel:")
    print(f"Nome do Cliente: {aluguel['cliente']}")
    print(f"Carro Alugado: {veiculo['modelo']} {veiculo['cor']}")
    print(f"Ar-condicionado: {'Sim' if acessorios['ar'] else 'Não'}")
    print(f"Direção Elétrica: {'Sim' if acessorios['direcao'] else 'Não'}")
    print(f"Vidro Elétrico: {'Sim' if acessorios['vidro-eletrico'] else 'Não'}")
    print(f"Quilometragem Rodada: {aluguel['quilometragem']} KM")
    print(f"Valor por KM: R${aluguel['valor']}")
    print(f"Total a ser pago: R${aluguel['quilometragem'] * aluguel['valor']}")


def visualizar_veiculos(veiculos):
    if len(veiculos) == 0:
        print("Não há veículos cadastrados.")
        return

    print("Veículos cadastrados:")
    for i, veiculo in enumerate(veiculos):
        print(f"{i} - {veiculo['modelo']} {veiculo['cor']} {'Alugado para ' + veiculo['alugueis'][-1]['cliente'] if veiculo['alugueis'] else 'Disponível'}")

    indice_veiculo = int(input("Informe o índice do veículo para detalhes (ou -1 para sair): "))
    if indice_veiculo == -1:
        return

    veiculo = veiculos[indice_veiculo]

    # Adicionando submenu
    while True:
        submenu_veiculo_escolha = int(input("Submenu Visualizar Veículos: \n"
                                            "1 - Visualizar detalhes \n"
                                            "2 - Voltar ao menu principal \n"
                                            "3 - Visualizar detalhes do aluguel \n"
                                            ": "))

        if submenu_veiculo_escolha == 1:
            detalhes_veiculo(veiculo)
        elif submenu_veiculo_escolha == 2:
            break
        elif submenu_veiculo_escolha == 3 and veiculo["alugueis"]:
            detalhes_aluguel(veiculo["alugueis"][-1], veiculo)
        else:
            print("Opção inválida. Tente novamente.")


def detalhes_veiculo(veiculo):
    print("\nDetalhes do veículo:")
    print(f"Modelo: {veiculo['modelo']}")
    print(f"Cor: {veiculo['cor']}")
    print(f"Ano: {veiculo['ano']}")
    print(f"Acessórios:")
    print(f"  - Ar-condicionado: {'Sim' if veiculo['acessorios']['ar'] else 'Não'}")
    print(f"  - Vidro Elétrico: {'Sim' if veiculo['acessorios']['vidro-eletrico'] else 'Não'}")
    print(f"  - Direção Elétrica: {'Sim' if veiculo['acessorios']['direcao'] else 'Não'}")
    print(f"Status: {'Alugado para ' + veiculo['alugueis'][-1]['cliente'] if veiculo['alugueis'] else 'Disponível'}")


def rodar():
    veiculos = ler_veiculos()
    while True:
        escolha = menu()
        if escolha == 1:
            veiculo = cadastrar_veiculo()
            veiculos.append(veiculo)
            escrever_veiculos(veiculos)
        elif escolha == 2:
            cadastrar_aluguel(veiculos)
            escrever_veiculos(veiculos)
        elif escolha == 3:
            visualizar_alugueis(veiculos)
        elif escolha == 4:
            visualizar_veiculos(veiculos)
        elif escolha == 0:
            break


if __name__ == "__main__":
    main()
    rodar()
