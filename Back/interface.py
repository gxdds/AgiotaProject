import tkinter as tk
from functions import coletar_dados_cliente, enviar_sms_cliente, identificar_parcelas
import openpyxl
import tkinter as tk
import datetime


def abrir_janela_addcliente():
    janela_add = tk.Toplevel()
    janela_add.geometry("600x300")
    janela_add.title('Adicionar Cliente')
    janela_add.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
    janela_add.columnconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)

    def add_button():
        nome = input_nome.get()
        numero = input_numero.get()
        valoremprestado = input_valoremprestado.get()
        porcentagem = input_porcentagem.get()
        dias = input_dias.get()
        parcelas = input_parcelas.get()

        if nome and numero and valoremprestado and porcentagem and dias and parcelas:
            if numero.isnumeric() and valoremprestado.isnumeric() and porcentagem.isnumeric() and dias.isnumeric() and parcelas.isnumeric():
                janela_mensagem = tk.Toplevel()
                janela_mensagem.geometry("500x50")
                janela_mensagem.rowconfigure(0, weight=1)
                janela_mensagem.columnconfigure(0, weight=1)
                janela_mensagem.title("Cliente adicionado com sucesso!")
                label_sucesso = tk.Label(janela_mensagem,
                                         text=f"O cliente {nome} com a 1° parcela para daqui {dias} dias foi adicionado com sucesso!")
                label_sucesso.grid(row=0, column=0, sticky="NSEW")
            else:
                janela_mensagem = tk.Toplevel()
                janela_mensagem.geometry("500x50")
                janela_mensagem.rowconfigure(0, weight=1)
                janela_mensagem.columnconfigure(0, weight=1)
                janela_mensagem.title("Erro")
                label_erro = tk.Label(janela_mensagem,
                                      text="O celular do cliente deve conter apenas números e sem espaços")
                label_erro.grid(row=0, column=0, sticky="NSEW")
        else:
            janela_mensagem = tk.Toplevel()
            janela_mensagem.geometry("500x50")
            janela_mensagem.rowconfigure(0, weight=1)
            janela_mensagem.columnconfigure(0, weight=1)
            janela_mensagem.title("Erro")
            label_erro = tk.Label(janela_mensagem, text="Erro em adicionar o cliente, confira os campos novamente")
            label_erro.grid(row=0, column=0, sticky="NSEW")

        return input_nome.get(), input_numero.get(), input_valoremprestado.get(), input_porcentagem.get(), input_dias.get(), input_parcelas.get()


    label_nome = tk.Label(janela_add, text="Digite o nome do cliente: ")
    input_nome = tk.Entry(janela_add)

    label_numero = tk.Label(janela_add, text="Digite o número do cliente (55+DDD+CEL): ")
    input_numero = tk.Entry(janela_add)

    label_valoremprestado = tk.Label(janela_add, text="Digite o valor emprestado ao cliente: ")
    input_valoremprestado = tk.Entry(janela_add)

    label_porcentagem = tk.Label(janela_add, text="Digite a porcentagem de juros: ")
    input_porcentagem = tk.Entry(janela_add)

    label_dias = tk.Label(janela_add, text="Digite a cada quanto tempo o cliente irá pagar (em dias): ")
    input_dias = tk.Entry(janela_add)

    label_parcelas = tk.Label(janela_add, text="Digite quantas parcelas serão: ")
    input_parcelas = tk.Entry(janela_add)

    botao_voltar = tk.Button(janela_add, text="Cancelar", command=janela_add.destroy, width=15, height=2)
    botao_adicionar = tk.Button(janela_add, text="Adicionar", command=add_button, width=15, height=2)

    #grids
    label_nome.grid(row=0, column=0)
    label_numero.grid(row=1, column=0)
    label_valoremprestado.grid(row=2, column=0)
    label_porcentagem.grid(row=3, column=0)
    label_dias.grid(row=4, column=0)
    label_parcelas.grid(row=5, column=0)

    input_nome.grid(row=0, column=1, sticky="WE")
    input_numero.grid(row=1, column=1, sticky="WE")
    input_valoremprestado.grid(row=2, column=1, sticky="WE")
    input_porcentagem.grid(row=3, column=1, sticky="WE")
    input_dias.grid(row=4, column=1, sticky="WE")
    input_parcelas.grid(row=5, column=1, sticky="WE")

    botao_voltar.grid(row=3, column=2, sticky="NSWE")
    botao_adicionar.grid(row=1, column=2, sticky="NSWE")



janela = tk.Tk()
janela.geometry("1200x700")
janela.title("SMSToday")


botao_adicionarcliente = tk.Button(janela, text="Adicionar novo cliente", command=abrir_janela_addcliente)
botao_adicionarcliente.grid(row=0, column=0)



janela.mainloop()







