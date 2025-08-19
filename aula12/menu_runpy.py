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
            runpy.run_path('5.py')
        elif opcao== '2':
            runpy.run_path('6.py')
        elif opcao== '3':
            runpy.run_path('7.py')
        elif opcao=='0':
            print('saindo do programa.')
            break
        else:
            print('opção invalida')

#iniciar o Menu
if __name__== "__main__":
    menu()
