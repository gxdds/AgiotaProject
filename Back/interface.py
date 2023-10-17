import tkinter as tk
from functions import coletar_dados_cliente, enviar_sms_cliente, identificar_parcelas
import openpyxl


# Função para adicionar usuário
def adicionar_usuario():
    dados_cliente = coletar_dados_cliente()
    # Atualize a interface ou exiba uma mensagem de sucesso

# Função para enviar SMS
def enviar_sms():
    clientes_match = identificar_parcelas()
    if clientes_match:
        for cliente in clientes_match:
            enviar_sms_cliente(cliente['Nome'], cliente['Celular'], cliente['Parcela'], cliente['Valor da Parcela'])
    # Atualize a interface ou exiba uma mensagem de sucesso

# Função para atualizar a Label da planilha
def atualizar_planilha_label():
    # Implemente a lógica para ler a planilha e exibir os dados aqui
    # Por exemplo, você pode usar a biblioteca openpyxl para ler a planilha
    # e, em seguida, atualizar a Label com os dados lidos
    pass

# Crie a janela principal
root = tk.Tk()
root.title("Nome do Programa")

# Crie uma Label para exibir a planilha
planilha_label = tk.Label(root, text="Aqui você pode exibir a planilha.")
planilha_label.pack()

# Crie um menu
menu = tk.Menu(root)
root.config(menu=menu)

# Menu "Usuário"
menu_usuario = tk.Menu(menu)
menu.add_cascade(label="Usuário", menu=menu_usuario)
menu_usuario.add_command(label="Adicionar Usuário", command=adicionar_usuario)

# Menu "SMS"
menu_sms = tk.Menu(menu)
menu.add_cascade(label="SMS", menu=menu_sms)
menu_sms.add_command(label="Enviar SMS", command=enviar_sms)

# Função para atualizar a Label da planilha
atualizar_planilha_label = tk.Button(root, text="Atualizar Planilha", command=atualizar_planilha_label)
atualizar_planilha_label.pack()

# Inicie a interface
root.mainloop()
