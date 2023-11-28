class ControleRemoto:
    def __init__(self, cor, altura, profundidade,largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    
controle1 = ControleRemoto("preto","10cm", "2cm","2cm")
print(controle1.altura)