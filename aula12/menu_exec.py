import runpy #importar o codigo de outro arquivo


def menu():
    while True:
        print('\n--menu de opçoes')
        print('1- converter metros para centimetros')
        print('2- calcular area do circulo')
        print('3- calcular area do quadrado')
        print('0- sair')
        
        opcao= input('escolha uma opçao:')
        if opcao == '1':
            exec(open("5.py").read())
        elif opcao== '2':
            exec(open("6.py").read())
        elif opcao== '3':
            exec(open("7.py").read())#OBRIGATORIO ""
        elif opcao=='0':
            print('saindo do programa.')
            break
        else:
            print('opção invalida')

#iniciar o Menu
if __name__== "__main__":
    menu()
