from tkinter import *
from tkinter import messagebox
from veiculos import Veiculo, salvar_dados, carregar_dados

veiculos = carregar_dados()


def cadastrar_veiculo():
    def salvar():
        # Obtendo os valores dos campos de entrada
        modelo = entry_modelo.get().strip()
        ano = entry_ano.get().strip()
        cor = entry_cor.get().strip()

        # Verificações para garantir que os campos obrigatórios não estejam vazios
        if not modelo:
            messagebox.showwarning("Aviso", "Por favor, insira o modelo do veículo.")
            return
        if not ano:
            messagebox.showwarning("Aviso", "Por favor, insira o ano do veículo.")
            return
        if not cor:
            messagebox.showwarning("Aviso", "Por favor, insira a cor do veículo.")
            return
        try:
            # Tentando converter o ano para inteiro para validar
            ano = int(ano)
        except ValueError:
            messagebox.showwarning("Aviso", "Por favor, insira um ano válido.")
            return

        # Se passar pelas verificações, prossegue com o cadastro
        acessorios = {
            'ar': var_ar.get(),
            'vidro_eletrico': var_vidro.get(),
            'direcao': var_direcao.get()
        }

        veiculo = Veiculo(modelo, ano, cor, acessorios)
        veiculos.append(veiculo)
        salvar_dados(veiculos)
        messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso.")
        janela_cadastro.destroy()

    janela_cadastro = Toplevel()
    janela_cadastro.title("Cadastrar Veículo")

    Label(janela_cadastro, text="Modelo:").pack()
    entry_modelo = Entry(janela_cadastro)
    entry_modelo.pack()

    Label(janela_cadastro, text="Ano:").pack()
    entry_ano = Entry(janela_cadastro)
    entry_ano.pack()

    Label(janela_cadastro, text="Cor:").pack()
    entry_cor = Entry(janela_cadastro)
    entry_cor.pack()

    var_ar = BooleanVar()
    Checkbutton(janela_cadastro, text="Ar condicionado", variable=var_ar).pack()

    var_vidro = BooleanVar()
    Checkbutton(janela_cadastro, text="Vidro elétrico", variable=var_vidro).pack()

    var_direcao = BooleanVar()
    Checkbutton(janela_cadastro, text="Direção hidráulica", variable=var_direcao).pack()

    Button(janela_cadastro, text="Salvar", command=salvar).pack()


def cadastrar_aluguel():
    def salvar():
        cliente = entry_cliente.get()
        valor = float(entry_valor.get())
        quilometragem = int(entry_quilometragem.get())
        veiculo_selecionado = veiculos[lista_veiculos.curselection()[0]]
        veiculo_selecionado.adicionar_aluguel(cliente, valor, quilometragem)
        salvar_dados(veiculos)
        janela_aluguel.destroy()

    janela_aluguel = Toplevel()
    janela_aluguel.title("Cadastrar Aluguel")

    Label(janela_aluguel, text="Cliente:").pack()
    entry_cliente = Entry(janela_aluguel)
    entry_cliente.pack()

    Label(janela_aluguel, text="Valor:").pack()
    entry_valor = Entry(janela_aluguel)
    entry_valor.pack()

    Label(janela_aluguel, text="Quilometragem:").pack()
    entry_quilometragem = Entry(janela_aluguel)
    entry_quilometragem.pack()

    Label(janela_aluguel, text="Selecionar Veículo:").pack()
    lista_veiculos = Listbox(janela_aluguel)
    for veiculo in veiculos:
        lista_veiculos.insert(END, veiculo.modelo)
    lista_veiculos.pack()

    Button(janela_aluguel, text="Salvar", command=salvar).pack()


def visualizar_alugueis():
    janela_alugueis = Toplevel()
    janela_alugueis.title("Aluguéis")

    tem_alugueis = False

    for veiculo in veiculos:
        if veiculo.alugueis:  # Verifica se há aluguéis para o veículo
            Label(janela_alugueis, text=f"Veículo: {veiculo.modelo}").pack()
            for aluguel in veiculo.alugueis:
                Label(janela_alugueis,
                      text=f"Cliente: {aluguel['cliente']}, Valor: {aluguel['valor']}, Quilometragem: {aluguel['quilometragem']}").pack()
            tem_alugueis = True

    if not tem_alugueis:  # Se não houver nenhum aluguel, exibe uma mensagem
        Label(janela_alugueis, text="Não há aluguéis registrados.").pack()


def visualizar_veiculos():
    janela_veiculos = Toplevel()
    janela_veiculos.title("Veículos")

    for veiculo in veiculos:
        texto = f"Modelo: {veiculo.modelo}, Ano: {veiculo.ano}, Cor: {veiculo.cor}, Acessórios: {', '.join([k for k, v in veiculo.acessorios.items() if v])}"
        Label(janela_veiculos, text=texto).pack()


def iniciar_interface():
    root = Tk()
    root.title("Sistema de Locadora de Veículos")

    # Definindo um tema de cores
    bg_color = "#f0f0f0"
    button_color = "#e1e1e1"
    text_color = "#000000"
    font_spec = ("Arial", 12)

    # Configurando o background da janela principal
    root.configure(bg=bg_color)

    # Frame para conter os botões e centralizá-los
    frame = Frame(root, bg=bg_color)
    frame.pack(expand=True, padx=20)

    # Botões para as funcionalidades com espaçamento e design melhorado
    Button(frame, text="Cadastrar Veículo", command=cadastrar_veiculo, width=20, height=2, bg=button_color,
           fg=text_color, font=font_spec).pack(pady=10, padx=20)
    Button(frame, text="Cadastrar Aluguel", command=cadastrar_aluguel, width=20, height=2, bg=button_color,
           fg=text_color, font=font_spec).pack(pady=10, padx=20)
    Button(frame, text="Visualizar Aluguéis", command=visualizar_alugueis, width=20, height=2, bg=button_color,
           fg=text_color, font=font_spec).pack(pady=10, padx=20)
    Button(frame, text="Visualizar Veículos", command=visualizar_veiculos, width=20, height=2, bg=button_color,
           fg=text_color, font=font_spec).pack(pady=10, padx=20)

    root.mainloop()
