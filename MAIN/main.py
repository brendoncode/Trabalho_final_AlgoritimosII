import interface

if __name__ == "__main__":
    """
    Quando o script é executado, se este for o módulo principal, a interface gráfica é iniciada.

    Este script atua como o ponto de entrada do programa, chamando a função que ativa a interface do usuário,
    onde as operações de gestão de veículos podem ser realizadas.

    A função iniciar_interface é responsável por criar a janela principal e carregar todos os componentes
    da interface gráfica do usuário, permitindo interações como cadastrar veículos, cadastrar aluguéis,
    visualizar aluguéis existentes e visualizar informações dos veículos.
    """
    interface.iniciar_interface()
