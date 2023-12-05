import unittest
from unittest.mock import patch, mock_open
from veiculos import Veiculo, salvar_dados, carregar_dados
import logging

# Configuração do logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class TestVeiculo(unittest.TestCase):

    def setUp(self):
        logging.info('Configurando o teste...')
        self.veiculo = Veiculo("TesteModelo", 2020, "Azul", {"ar": True, "vidro_eletrico": True, "direcao": True})
        logging.info('Veiculo configurado para teste.')

    def test_adicionar_aluguel(self):
        logging.info('Iniciando teste de adicionar_aluguel...')
        self.veiculo.adicionar_aluguel("ClienteTeste", 100.0, 1500)
        self.assertEqual(len(self.veiculo.alugueis), 1)
        logging.info('Aluguel adicionado com sucesso.')
        self.assertEqual(self.veiculo.alugueis[0]["cliente"], "ClienteTeste")
        logging.info('Cliente verificado com sucesso.')

    @patch('veiculos.open', new_callable=mock_open)
    def test_salvar_dados(self, mock_file):
        logging.info('Iniciando teste de salvar_dados...')
        salvar_dados([self.veiculo])
        mock_file.assert_called_once_with('veiculos.json', 'w')
        mock_file().write.assert_called()
        logging.info('Teste de salvar_dados concluído com sucesso.')

    @patch('veiculos.json.load')
    @patch('veiculos.open', new_callable=mock_open)
    def test_carregar_dados(self, mock_file, mock_json_load):
        logging.info('Iniciando teste de carregar_dados...')
        mock_json_load.return_value = [
            {
                "modelo": "TesteModelo",
                "ano": 2020,
                "cor": "Azul",
                "acessorios": {"ar": True, "vidro_eletrico": True, "direcao": True},
                "alugueis": []
            }
        ]
        result = carregar_dados()
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Veiculo)
        logging.info('Teste de carregar_dados concluído com sucesso.')


# Para rodar os testes
if __name__ == '__main__':
    unittest.main()
