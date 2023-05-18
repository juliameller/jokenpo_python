import random
from time import sleep

opcoes = ['pedra', 'papel', 'tesoura']
placar_computador = 0
placar_usuario = 0

while True:
    print('----------Jokenpo----------')
    print('Pedra')
    print('Papel')
    print('Tesoura')
    print('-'*26)
    opcao_usuario = input('Escolha uma opção: ')
    opcao_usuario_lower = opcao_usuario.lower()

    if opcao_usuario_lower not in opcoes:
        print('Opção inválida!')
        continue

    opcao_computador = random.choice(opcoes)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    sleep(0.5)

    print('Sua jogada:', opcao_usuario_lower)
    print('Jogada do computador:', opcao_computador)
    print('-'*26)

    if opcao_usuario_lower == 'pedra':
        if opcao_computador == 'pedra':
            print('Empate!')
        elif opcao_computador == 'papel':
            print('Você perdeu!')
            placar_computador += 1
        elif opcao_computador == 'tesoura':
            print('Você ganhou!')
            placar_usuario += 1
        
    if opcao_usuario_lower == 'papel':
        if opcao_computador == 'papel':
            print('Empate!')
        elif opcao_computador == 'tesoura':
            print('Você perdeu!')
            placar_computador += 1
        elif opcao_computador == 'pedra':
            print('Você ganhou!')
            placar_usuario += 1

    if opcao_usuario_lower == 'tesoura':
        if opcao_computador == 'tesoura':
            print('Empate!')
        elif opcao_computador == 'pedra':
            print('Você perdeu!')
            placar_computador += 1
        elif opcao_computador == 'papel':
            print('Você ganhou!')
            placar_usuario += 1
    
    print(f'Placar: Você {placar_usuario} X Computador {placar_computador}')



