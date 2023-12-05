import json


class Veiculo:
    """
    Classe representando um veículo dentro do sistema de locadora de veículos.

    Atributos:
        modelo (str): Modelo do veículo.
        ano (int): Ano de fabricação do veículo.
        cor (str): Cor do veículo.
        acessorios (dict of str: bool): Dicionário contendo a disponibilidade dos acessórios.
        alugueis (list of dict): Lista de aluguéis associados ao veículo.

    Métodos:
        adicionar_aluguel: Adiciona um novo aluguel à lista de aluguéis do veículo.
    """

    def __init__(self, modelo, ano, cor, acessorios, alugueis=None):
        """
        Inicializa uma nova instância da classe Veiculo.

        Parâmetros:
            modelo (str): Modelo do veículo.
            ano (int): Ano de fabricação do veículo.
            cor (str): Cor do veículo.
            acessorios (dict of str: bool): Dicionário contendo a disponibilidade dos acessórios.
            alugueis (list of dict): Lista de aluguéis associados ao veículo (padrão é None, que cria uma lista vazia).
        """
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.acessorios = acessorios
        self.alugueis = alugueis if alugueis is not None else []

    def adicionar_aluguel(self, cliente, valor, quilometragem):
        """
        Adiciona um novo aluguel à lista de aluguéis do veículo.

        Parâmetros:
            cliente (str): Nome do cliente que realizou o aluguel.
            valor (float): Valor do aluguel.
            quilometragem (int): Quilometragem do veículo no momento do aluguel.
        """
        self.alugueis.append({
            'cliente': cliente,
            'valor': valor,
            'quilometragem': quilometragem
        })


def salvar_dados(veiculos):
    """
    Salva a lista de veículos em um arquivo JSON.

    Parâmetros:
        veiculos (list of Veiculo): Lista de veículos para salvar no arquivo.
    """
    with open('veiculos.json', 'w') as arquivo:
        json.dump([veiculo.__dict__ for veiculo in veiculos], arquivo)


def carregar_dados():
    """
    Carrega a lista de veículos de um arquivo JSON.

    Retorna:
        list of Veiculo: Lista de veículos carregados do arquivo.
    """
    try:
        with open('veiculos.json', 'r') as arquivo:
            dados = json.load(arquivo)
            return [Veiculo(veiculo['modelo'], veiculo['ano'], veiculo['cor'], veiculo['acessorios'],
                            veiculo.get('alugueis', [])) for veiculo in dados]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
