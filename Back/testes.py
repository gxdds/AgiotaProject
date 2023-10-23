from datetime import datetime, timedelta
lista_data_cadastro = []
data_hoje = datetime.now()
data_hoje_form1 = datetime.strftime(data_hoje, "%d/%m/%y")
data_hoje_form2 = datetime.strptime(data_hoje_form1, "%d/%m/%y")
lista_data_cadastro.append(data_hoje_form2)

print(lista_data_cadastro)
print(data_hoje_form2)
print(data_hoje_form1)