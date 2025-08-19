class carro:
    def __init__(self, nome):
        self.nome= nome 
    
    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca= carro('fusca')
print('nome:',fusca.nome)
fusca.acelerar()

byd= carro('byd')
print('nome:',byd.nome)
byd.acelerar()
