# ARRUMAR!!!!
# fazer dar empate - FEITO
# arrumar o número de turnos - FEITO
# adicionar turnos de verdade - FEITO
# adicionar cores - FEITO
# ajustar volume - FEITO
# guarda dando dano mesmo com vida negativa - FEITO

import random
import os
import pygame
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.4)

def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')

def oguarda():

    # CORES
    branco = '\033[0;30m'
    vermelho = '\033[1;31m'
    verde = '\033[32m'
    ciano = '\033[36m'
    limpo = '\033[0;37m'

    # VIDA
    vida =  100
    gvida = 100

    # POÇÕES
    curaquant = 3

# ENTRADA >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    pygame.mixer.music.load('music/melodia.mp3')
    pygame.mixer.music.play()
    print('\n \n')
    print('='*93)
    print()
    print ((' '*29) , '-----O guarda está repousando-----')
    print()
    print(' '*44 , '')
    print(r' '*43 , r'/‾‾‾‾\ ')
    print(r' '*42 , r'( -  - )')
    print(r' '*43 , r'\____/')
    print(r' '*43 , r'/|//|\ ')
    print(r' '*40 , r'|_/ |//| |‾| ')
    print(r' '*38 , r' ===  |//| |/|')
    print(r' '*39 , r' ‖  (0000) V')
    print(r' '*40 , r'‖   ||||')
    print(r' '*40 , r'v   ||||')
    print(r' '*43 , r'/_||_\ ')
    print(' '*43 , )
    print(' '*43 , )
    print(' '*43 , )
    input('--> Aperte ENTER para prosseguir')

    limpartela()

    print('\n \n')
    print('='*93)
    print()
    print()
    print ((' '*50) , 'Alto lá!')
    print(' '*50 , ' /')
    print(r' '*43 , r'/‾‾‾‾\ ')
    print(r' '*42 , r'( Ô  Ô )')
    print(r' '*43 , r'\____/')
    print(r' '*43 , r'/|//|\ ')
    print(r' '*40 , r'|_/ |//| |‾| ')
    print(r' '*38 , r' ===  |//| |/|')
    print(r' '*39 , r' ‖  (0000) V')
    print(r' '*40 , r'‖   ||||')
    print(r' '*40 , r'v   ||||')
    print(r' '*43 , r'/_||_\ ')
    print(' '*43 , )
    print(' '*43 , )
    print(' '*43 , )
    input('--> Aperte ENTER para prosseguir')

    limpartela()

    print('\n \n')
    print('='*93)
    print()
    print()
    print(' '*50 , f'{vermelho}Não deixarei ninguém passar!{limpo}')
    print(' '*50 , ' /')
    print(r' '*43 , r'/‾‾‾‾\ ')
    print(r' '*42 , r'( Ò  Ó )')
    print(r' '*43 , r'\____/')
    print(r' '*43 , r'/|//|\ ')
    print(r' '*40 , r'|_/ |//| |‾| ')
    print(r' '*38 , r' ===  |//| |/|')
    print(r' '*39 , r' ‖  (0000) V')
    print(r' '*40 , r'‖   ||||')
    print(r' '*40 , r'v   ||||')
    print(r' '*43 , r'/_||_\ ')
    print(' '*43 , )
    print(' '*43 , )
    print(' '*43 , )
    input('--> Aperte ENTER para prosseguir')

    limpartela()

    pygame.mixer.music.load('music/boss.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)
#FIM DA ENTRADA >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #checagem de turnos
    turno = 0
    chturno = 1
    if chturno == 3:
        chturno = 1


    while vida > 0 and gvida > 0:

        if chturno == 1:

            # TURNOS
            turno = turno + 1

            # DANO
            dano= random.randint(5, 15)
            gdano= random.randint(10, 20)

            # CURA
            curavalor = random.randint(20 , 30)

            escolha = '0'
            print('\n \n')
            print('='*93)
            print()
            print(' '*41 , 'EM BATALHA!')
            print(' '*43 , f'{ciano}TURNO {turno}{limpo}')
            print()
            print(' '*20 , r'                    ^  /‾‾‾‾\    ')
            print(' '*20 , r'                    ‖ ( Ò  Ó )   ')
            print(' '*20 , r'                    ‖  \____/    ')
            print(' '*20 , r'                   === /|//|\|‾| ')
            print(' '*20 , r'                    |_/ |//| |/| ')
            print(' '*20 , r'                        |//|  V  ')
            print(' '*20 , r'                       (0000)    ')
            print(' '*20 , r'                        ||||     ')
            print(' '*20 , r'                        ||||     ')
            print(' '*20 , r'                       /_||_\    ')
            print(f'\nSua vida : {vida}' )
            print(f'Vida do Guarda : {gvida}')
            print(f'Poções no bolso: {curaquant}')
            print()
            escolha = str(input('Escolha a opção que deseja:\n \n      (1) Atacar - Causa de 5 a 20 de dano\n      (2) Poção -  Cura de 20 a 30 de vida\n                    '))


            if escolha == '1':
                limpartela()
                gvida -= dano
                print('\n \n')
                print('='*93)
                print()
                print(' '*40 , 'Você atacou!')
                print(' '*43 , f'{ciano}TURNO {turno}{limpo}')
                print()
                print(' '*20 , rf'                    ^  {vermelho}/‾‾‾‾\{limpo}    ')
                print(' '*20 , rf'                    ‖ {vermelho}( ^  O ){limpo}   ')
                print(' '*20 , rf'                    ‖  {vermelho}\____/{limpo}    ')
                print(' '*20 , rf'                   === {vermelho}/|//|\{limpo}|‾| ')
                print(' '*20 , rf'                    |{vermelho}_/ |//|{limpo} |/| ')
                print(' '*20 , rf'                        {vermelho}|//|{limpo}  V  ')
                print(' '*20 , rf'                       {vermelho}(0000){limpo}    ')
                print(' '*20 , rf'                        {vermelho}||||{limpo}     ')
                print(' '*20 , rf'                        {vermelho}||||{limpo}     ')
                print(' '*20 , rf'                       {vermelho}/_||_\{limpo}    ')
                print(f'\nSua vida: {vida}')
                print(f'Vida do Guarda : {gvida}')
                print()
                print(f'{ciano}Você deu {dano} de dano no guarda!{limpo}\n')
                input('Pressione ENTER para continuar...')
                limpartela()
                if gvida > 0:
                    chturno = chturno + 1
                else:
                    chturno = 0

            if escolha == '2':
                if curaquant >0:
                    vida += curavalor
                    curaquant -= 1
                    print(f'{verde}Você curou {curavalor} de vida!{limpo}\n')
                    input('Pressione ENTER para continuar...')

                    if vida > 100:
                        input("Sua vida está no máximo, sua poção foi gasta... Enter para prosseguir")
                        vida = 100
                        chturno = chturno + 1
                else:
                    input('Você não tem mais curas! Perdeu a vez... aperte ENTER para continuar')
                    chturno = chturno + 1

            limpartela()


        if chturno == 2:

            # TURNOS
            turno = turno + 1

            # DANO
            gdano= random.randint(10, 20)
            vida -= gdano

            # CURA
            curavalor = random.randint(20 , 30)

            print('\n \n')
            print('='*93)
            print()
            print(' '*41 , 'ELE ATACOU!')
            print(' '*43 , f'{vermelho}TURNO {turno}{limpo}')
            print()
            print(' '*20 , r'                  ^    /‾‾‾‾\    ')
            print(' '*20 , r'                  ‖   ( Ò  Ó )   ')
            print(' '*20 , r'                   ‖   \____/    ')
            print(' '*20 , r'                   === /|//|\|‾| ')
            print(' '*20 , r'                    |_/ |//| |/| ')
            print(' '*20 , r'                        |//|  V  ')
            print(' '*20 , r'                       (0000)    ')
            print(' '*20 , r'                        ||||     ')
            print(' '*20 , r'                        ||||     ')
            print(' '*20 , r'                       /_||_\    ')
            print(f'\nSua vida: {vida}')
            print(f'Vida do Guarda : {gvida}')
            print()
            print(f'{vermelho}Ele te deu {gdano} de dano!{limpo}\n')
            input('Pressione ENTER para continuar...')

            limpartela()
            chturno = 1


#vencendo, morrendo ou empatando
        if gvida <= 0:
            limpartela()
            pygame.mixer.music.load('music/ganhou.mp3')
            pygame.mixer.music.play()
            print(f'\nSua vida : {vida}' )
            print(f'Vida do Guarda : {gvida}\n')
            print('              |================|')
            print('              |  VC VENCEU!:D  |')
            print('              |================|')
            print()
            input('--> Aperte ENTER para fechar')
            break

        if vida <= 0:
            limpartela()
            pygame.mixer.music.load('music/perdeu.mp3')
            pygame.mixer.music.play()
            print(f'Sua vida : {vida}' )
            print(f'Vida do Guarda : {gvida}\n')
            print('              |================|')
            print('              | Você morreu!:c |')
            print('              |================|')
            print()
            input('--> Aperte ENTER para fechar')
            break

        if vida <= 0 and vida == gvida:
            limpartela()
            print(f'Sua vida : {vida}' )
            print(f'Vida do Guarda : {gvida}\n')
            print('              |================|')
            print('              |    EMPTATE!    |')
            print('              |================|')
            print()
            input('--> Aperte ENTER para fechar')

oguarda()
