class pessoa:
    def __init__(self , nome , sobrenome) ->None:
        self.nome = nome
        self.sobrenome= sobrenome

p1 = pessoa('andre','marques')
p2= pessoa ('gilmar','santos')
print (p1.nome)  
print (p2.nome)
print('------')
print (p2.nome)
print (p2.sobrenome)