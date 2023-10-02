valor = 1000
parcelas = 5
porcentagem = 30

valor_total = valor
valor_parcela = (valor_total / parcelas) + (porcentagem / 100 * valor)
print(valor_parcela)