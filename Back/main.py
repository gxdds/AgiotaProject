from functions import coletar_dados_cliente, adicionar_dados_planilha_local, identificar_parcelas, enviar_sms_cliente
import openpyxl


if __name__ == "__main__":
    # Colete os dados do cliente
    cliente, nmr_cliente, valor, porcentagem, intervalo_pagamentos, parcelas, formatted_valor_parcela, total_a_pagar, data_formatada = coletar_dados_cliente()


    # Adicione os dados à planilha local
    adicionar_dados_planilha_local()

    clientes_match = identificar_parcelas()
    if clientes_match:
        for cliente in clientes_match:
            print(f"Nome: {cliente['Nome']}")
            print(f"Celular: {cliente['Celular']}")
            print(f"Parcela: {cliente['Parcela']}")
            print(f"Valor da Parcela: {cliente['Valor da Parcela']}")
            print("-" * 30)
            enviar_sms_cliente(nome_cliente=cliente['Nome'], numero_celular=cliente['Celular'], numero_parcela=cliente['Parcela'], valor_parcela=cliente['Valor da Parcela'])
    else:
        print("Nenhum cliente corresponde aos critérios.")
