
def calcular_desconto(valor_original, percentual_desconto):
    if percentual_desconto > 100 or percentual_desconto < 0:
        raise ValueError("O desconto não pode ser maior que zero ou maior que 100")
    
    if valor_original <= 0:
        raise ValueError("O preço do produto deve ser maior que zero.")
    
    desconto = valor_original * (percentual_desconto / 100)
    
    if desconto >= valor_original:
        return 0

    else:
        valor_com_desconto = valor_original - desconto 
        return valor_com_desconto

