print("insira o preço da mercadoria a seguir")
mercadoria = int(input("Qual o valor da mercadoria: \n"))

def desconto_mercadoria(mercadoria):
    if mercadoria >= 500:
        print(f"Seu produto irá receber 15% de desconto, em reais R${mercadoria-(mercadoria*15/100)}")
    elif mercadoria >= 250:
        print(f"Seu produto irá receber 8% de desconto, em reais R${mercadoria-(mercadoria*8/100)}")
    else:
        print("não será possivel oferecer descontos")
    
desconto_mercadoria(mercadoria)




