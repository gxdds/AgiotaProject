from functions import coletar_dados_cliente, fazer_upload_para_dropbox, calculo_parcelas, sms_planilha_info
from datetime import datetime, timedelta

if __name__ == "__main__":
    # Chame a função coletar_dados_cliente para coletar os dados do cliente
    #data_cadastro, intervalo_pagamentos, parcelas = coletar_dados_cliente()

    # Chame a função fazer_upload_para_dropbox para fazer upload dos dados do cliente para a planilha no Dropbox
    #fazer_upload_para_dropbox()

    # Converte data_cadastro em um objeto datetime
    #data_cadastro = datetime.strptime(data_cadastro, "%d/%m/%y")

    # Em seguida, chame a função calculo_parcelas com os argumentos corretos
    #datas_envio_sms = calculo_parcelas(data_cadastro, intervalo_pagamentos, parcelas)

    # chamar função sms_planilha_info para enviar o sms
    sms_planilha_info()