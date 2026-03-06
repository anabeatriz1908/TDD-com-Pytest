def calcular_valor_estacionamento(tempo_em_minutos):
    if tempo_em_minutos <= 0:
        raise ValueError("O tempo não pode ser menor ou igual a zero")

    valor_total = 0

    if tempo_em_minutos <= 60:
        valor_total += 10
        return valor_total
    

    #Calculando o valor total para o tempo acima de 60 minutos
    if tempo_em_minutos > 60:
        valor_total += 10
        tempo_em_minutos -= 60

    while tempo_em_minutos > 0:
        valor_total += 5
        tempo_em_minutos -= 60
    
    if valor_total >= 50:
        valor_total = 50

    return valor_total