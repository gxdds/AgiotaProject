from functions import coletar_dados_cliente, adicionar_dados_planilha_local, identificar_parcelas, enviar_sms_cliente
import openpyxl


if __name__ == "__main__":
    # Colete os dados do cliente
    #cliente, nmr_cliente, valor, porcentagem, intervalo_pagamentos, parcelas, formatted_valor_parcela, total_a_pagar, data_formatada = coletar_dados_cliente()


    # Adicione os dados à planilha local
    #adicionar_dados_planilha_local()

    clientes_com_sms_hoje = []
    clientes_match = identificar_parcelas()

    if clientes_match:
        for cliente in clientes_match:
            # Extraia as informações relevantes do cliente
            nome = cliente['Nome']
            celular = cliente['Celular']
            parcela = cliente['Parcela']
            valor_parcela = cliente['Valor da Parcela']

            # Calcule o valor total com base no número da parcela
            valor_total = parcela * valor_parcela

            # Adicione as informações do cliente à lista
            cliente_info = {
                'Nome': nome,
                'Celular': celular,
                'Parcela': parcela,
                'Valor da Parcela': valor_parcela,
                'Valor Total': valor_total
            }
            clientes_com_sms_hoje.append(cliente_info)

    if clientes_com_sms_hoje:
        print(clientes_com_sms_hoje)
    else:
        print("Nenhum cliente para enviar SMS hoje.")
