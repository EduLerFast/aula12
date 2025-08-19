class animal:
    def __init__ (self,nome,peso,idade) ->None:
        self.nome = nome 
        self.peso = peso
        self.idade = idade       
    def comendo(self):
        print(f'{self.nome} está comendo')



g= animal ('girafa','999 kg' , ' 10') 
print ('nome',g.nome)
print ('peso',g.peso)
print ('idade',g.idade)

ga= animal ('gato','2 kg' , ' 5') 
print ('nome',g.nome)
print ('peso',g.peso)
print ('idade',g.idade)

l= animal ('leao','200 kg' , ' 40') 
print ('nome',g.nome)
print ('peso',g.peso)
print ('idade',g.idade)