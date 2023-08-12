import os

palavra_secreta = 'pudim'
letras_acertadas = ''
tentativas = 0



while True:
    palavra = str(input('Digite uma letra: '))
    tentativas +=1

    if len(palavra) > 1:
        print('Digite apenas UMA letra')
        continue

    if palavra in palavra_secreta:
        letras_acertadas += palavra

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else: 
            palavra_formada += '*'
    print(palavra_formada)

    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!!!!')
        print('A palavra era', palavra_secreta)
        print('Tentativas: ', tentativas)
        break
