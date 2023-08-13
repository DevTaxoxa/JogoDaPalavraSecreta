lista = []
def Apagar_terminal():
    import os
    os.system('cls')
    return

while True:
    print('Selecione Uma Opção')
    opcao = str(input('[i]nseir  [a]pagar  [l]istar  [s]air: '))
    opcoes = ['i', 'a', 'l', 's']
    
    if opcao == 'i':
        novo_valor = input('Item: ')
        lista.append(novo_valor)
        Apagar_terminal()
        print('Valor adicionado!')
    
    elif opcao == 'a':   
        apagar_valor = (input('Escolha o indice para apagar: '))
        try:
            lista.pop(apagar_valor)
            print('Valor apagado!')
        except:
            print('Não foi possivel apagar esse indice')

    elif opcao == 'l':
        if lista == []:
            Apagar_terminal()
            print('Nada para listar!')
            
            
        for indice, nome in enumerate(lista):
            print(indice, nome)
        print('')

    elif opcao == 's':
        print('Até uma próxima! 😣')
        break
    
    else:
        print('Escolha, i, a, l, ou s. Por favor!')