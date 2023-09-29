from functions import coletar_dados_cliente, adicionar_dados_planilha_local, calculo_parcelas, sms_planilha_info
from datetime import datetime, timedelta

if __name__ == "__main__":
    # Colete os dados do cliente
    #cliente, nmr_cliente, valor, porcentagem, intervalo_pagamentos, parcelas, formatted_valor_parcela, total_a_pagar, data_formatada = coletar_dados_cliente()

    # Adicione os dados à planilha local
    #adicionar_dados_planilha_local()

    # Chame a função para calcular as datas de envio de SMS e obter informações adicionais
    infos_envio_sms = calculo_parcelas()

    if infos_envio_sms:
        print("As seguintes informações de envio de SMS de cobrança devem ser enviadas hoje:")
        for info in infos_envio_sms:
            nome, telefone, valor, numero = info
            print(f"Nome: {nome}, Telefone: {telefone}, Valor da Parcela: R${valor}, Parcela n°: {numero}")
    else:
        print("Nenhuma informação de envio de SMS de cobrança para hoje.")