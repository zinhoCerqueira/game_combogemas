import numpy as np
import random

#Das 10 letras possiveis, aqui eu seto a quantidade de letras que vão para o jogo.
def sortLetrasJogaveis(letras, qtd):
    
    count = 0
    retorno = []
    while count < qtd:
        sorteada = random.choice(letras)
        retorno.append(sorteada)
        letras.remove(sorteada)
        count += 1

    return retorno

#Verifica se tem uma jogada no mapa, caso não, o jogo se encerra.
def havePlay(mapa):

    linha = len(mapa)
    coluna = len(mapa[0])

    for i in range(linha):
        for j in range(coluna):

            if i == 0 and j == 0 :
                if swapDica(mapa, i, j, 'd') or swapDica(mapa, i, j, 's'):
                    return True

            elif i == 0 and j != 0:
                if swapDica(mapa, i, j, 'a') or swapDica(mapa, i, j, 'd') or swapDica(mapa, i, j, 's'):
                    return True

            elif i != 0 and j == 0:
                if swapDica(mapa, i, j, 'w') or swapDica(mapa, i, j, 's') or swapDica(mapa, i, j, 'd'):
                    return True

            elif i == linha and j == coluna:
                if swapDica(mapa, i, j, 'a') or swapDica(mapa, i, j, 'w'):
                    return True

            else:
                if swapDica(mapa, i, j, 'a') or swapDica(mapa, i, j, 'd') or swapDica(mapa, i, j, 'w') or swapDica(mapa, i, j, 's'):
                    return True
    
    return False

#Aqui eu seto o jogada, principalmente a segunda posição em que haverá a permutação.
#E caso tenha havido a jogada eu permuto e retiro o combo, caso não, só devolvo o mapa pro jogador.
def lance(mapa, play, pontuacao, letrasJogaveis):

    local1 = []
    local2 = []

    local1.append(play[0])
    local1.append(play[1])

    if play[2] == 'w':
        local2.append(play[0] - 1)
        local2.append(play[1])
    elif play[2] == 's':
        local2.append(play[0] + 1)
        local2.append(play[1])
    elif play[2] == 'a':
        local2.append(play[0])
        local2.append(play[1] -1 )
    elif play[2] == 'd':
        local2.append(play[0])
        local2.append(play[1] + 1)

    mapa = swap(local1, local2, mapa)

    if verificaComboNoMapa(mapa):
        resp  = 'Teve combo'
        mapa, pontuacao = analisisMap(mapa, pontuacao, letrasJogaveis)
    else:
        mapa = swap(local1, local2, mapa)
        resp = 'Não teve combo'

    return mapa, pontuacao, resp

#Troca de lugar 2 variaveis dentro do mapa.
def swap(l1, l2, mapa_function):
    mapa_function[l1[0],l1[1]], mapa_function[l2[0], l2[1]] =  mapa_function[l2[0], l2[1]], mapa_function[l1[0],l1[1]]
    return mapa_function

# Analisa se há combos gerado pelo gerador automatico de gemas.
def firstAnalisisMap(mapa, letrasjogaveis):

    linha = len(mapa)
    coluna = len(mapa[0])

    for i in range(linha):
        for j in range(coluna):
            if j + 2 < coluna :
                if mapa[i,j] == mapa[i,j+1] == mapa[i,j+2]:

                    mapa[i,j] = ' '
                    mapa[i,j+1] = ' '
                    mapa[i,j+2] = ' '
            if i + 2 < linha :
                if mapa[i,j] == mapa[i+1,j] == mapa[i+2,j]:
                    
                    mapa[i,j] = ' '
                    mapa[i + 1,j] = ' '
                    mapa[i + 2,j] = ' '

    mapa = reposition(mapa, letrasjogaveis)

    while verificaComboNoMapa(mapa) :
        mapa = firstRetiraCombo(mapa)
        mapa = reposition(mapa, letrasjogaveis)
    
    return mapa, True

# Repõe gemas nos lugares vazios.
def reposition(mapa, letrasjogaveis):

    linha = len(mapa)
    coluna = len(mapa[0])

    for i in range(linha):
        for j in range(coluna):
            if mapa[i,j] == ' ':
                mapa[i,j] = random.choice(letrasjogaveis)
    
    
    return mapa

# Retorna true e false casa haja um combo no mapa.
def verificaComboNoMapa(mapa):

    linha = len(mapa)
    coluna = len(mapa[0])

    for i in range(linha):
        for j in range(coluna):
            if j + 2 < coluna :
                if mapa[i,j] == mapa[i,j+1] == mapa[i,j+2]:
                    return True
            if i + 2 < linha :
                if mapa[i,j] == mapa[i+1,j] == mapa[i+2,j]:
                    return True
    
    return False

# Retira combos do mapa
def firstRetiraCombo(mapa):
    
    linha = len(mapa)
    coluna = len(mapa[0])

    for i in range(linha):
        for j in range(coluna):
            if j + 2 < coluna :
                if mapa[i,j] == mapa[i,j+1] == mapa[i,j+2]:

                    mapa[i,j] = ' '
                    mapa[i,j+1] = ' '
                    mapa[i,j+2] = ' '

            if i + 2 < linha :
                if mapa[i,j] == mapa[i+1,j] == mapa[i+2,j]:
                    
                    mapa[i,j] = ' '
                    mapa[i + 1,j] = ' '
                    mapa[i + 2,j] = ' '
    
    return mapa

# Retira combos do mapa, porém agora com a pontuação.
def retiraCombo(mapa, pontuacao):
    
    linha = len(mapa)
    coluna = len(mapa[0])

    for i in range(linha):
        for j in range(coluna):
            if j + 2 < coluna :
                if mapa[i,j] == mapa[i,j+1] == mapa[i,j+2]:

                    mapa[i,j] = ' '
                    mapa[i,j+1] = ' '
                    mapa[i,j+2] = ' '
                    pontuacao += 3

            if i + 2 < linha :
                if mapa[i,j] == mapa[i+1,j] == mapa[i+2,j]:
                    
                    mapa[i,j] = ' '
                    mapa[i + 1,j] = ' '
                    mapa[i + 2,j] = ' '
                    pontuacao += 3
    
    return mapa, pontuacao

# Analisa o mapa com o auxilio de outras funções para ver se tem um combo
# e retira-lo do mapa.
def analisisMap(mapa, pontuacao, letrasJogaveis):

    while verificaComboNoMapa(mapa):
        mapa, pontuacao = retiraCombo(mapa, pontuacao)
        mapa = gravidade(mapa, letrasJogaveis)

    return mapa, pontuacao

# Faz a queda das gemas acontecerem de acordo com uma "gravidade" que faz as peças 
# da matriz "cairem" e gera aleatoriamente se elas forem da primeira linha.
def gravidade(mapa, letrasJogaveis):

    linha = len(mapa)
    coluna = len(mapa[0])

    while voidLocal(mapa):
        for i in range(linha):
            for j in range(coluna):

                if mapa[i,j] == ' ' and i == 0:
                    mapa[i,j] = random.choice(letrasJogaveis)
                elif mapa[i,j] == ' ' and i != 0:
                    mapa[i,j] = mapa[i-1,j]
                    mapa[i-1, j] = ' '
    
    return mapa

# Verifica se alguma coordenada do mapa esteja vazia.
def voidLocal(mapa):
    
    linha = len(mapa)
    coluna = len(mapa[0])

    for i in range(linha):
        for j in range(coluna):
            if mapa[i,j] == ' ':
                return True
    
    return False

#Verifica as possibilidades de jogada para a dica.
def swapDica(mapa, x, y, direction):

    local1 = []
    local2 = []

    local1.append(x)
    local1.append(y)

    if direction == 'w':
        local2.append(x - 1)
        local2.append(y)
    elif direction == 's':
        local2.append(x + 1)
        local2.append(y)
    elif direction == 'a':
        local2.append(x)
        local2.append(y - 1)
    elif direction == 'd':
        local2.append(x)
        local2.append(y + 1)

#Gambiarra
    mapa = swap(local1, local2, mapa)

    resp = verificaComboNoMapa(mapa)

    mapa = swap(local1, local2, mapa)
    return resp

#Retorna o local exato da dica. Onde esta o elemento que pode fazer uma jogada.
def localDica(mapa):

    linha = len(mapa)
    coluna = len(mapa[0])

    for i in range(linha):
        for j in range(coluna):

            if i == 0 and j == 0 :
                if swapDica(mapa, i, j, 'd') or swapDica(mapa, i, j, 's'):
                    return i+1,j+1

            elif i == 0 and j != 0:
                if swapDica(mapa, i, j, 'a') or swapDica(mapa, i, j, 'd') or swapDica(mapa, i, j, 's'):
                    return i+1,j+1

            elif i != 0 and j == 0:
                if swapDica(mapa, i, j, 'w') or swapDica(mapa, i, j, 's') or swapDica(mapa, i, j, 'd'):
                    return i+1,j+1

            elif i == linha and j == coluna:
                if swapDica(mapa, i, j, 'a') or swapDica(mapa, i, j, 'w'):
                    return i+1,j+1

            else:
                if swapDica(mapa, i, j, 'a') or swapDica(mapa, i, j, 'd') or swapDica(mapa, i, j, 'w') or swapDica(mapa, i, j, 's'):
                    return i+1,j+1

    return -1, -1

#MAIN
def main():

    #variaveis vinda do jogador
    linha = int(input("Informe a quantidade de linhas do mapa > "))
    coluna = int(input("Informe a quantidade de colunas do mapa > "))
    qtdCores = int(input("Qual a quantidade de gemas o jogo terá >  "))

    #variaveis do jogo
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    letrasJogaveis = sortLetrasJogaveis(letras, qtdCores)
    mapa = np.empty((linha, coluna), dtype = str)
    pontuacao = 0

    #DISTRIBUIÇÂO DAS LETRAS NO MAPA
    for i in range(linha):
        for j in range(coluna):
            mapa[i,j] = random.choice(letrasJogaveis)

    verification = False

    while verification == False :
        mapa, verification = firstAnalisisMap(mapa, letrasJogaveis)

    #AQUI COMEÇA O JOGO
    while havePlay(mapa):

        if pontuacao > -1000:

            print("")
            print(mapa)

            print("")
            print("Quer uma dica ?")
            dica = input("Press x > ")
            if dica == 'x':
                d1, d2 = localDica(mapa)
                print("X > ", d1 ,'||||', "Y > ", d2)
                pontuacao -= 10

        print("Pontuação >>> ", pontuacao)
        print("")
        print(mapa)

        pos_x = int(input("Informe a LINHA do elemento > "))
        pos_y = int(input("Informe a COLUNA do elemento > "))
        direction = str(input("Informe a DIREÇÂO da jogada > "))
        play = [pos_x - 1, pos_y - 1, direction]

        list_direction = ['w', 's', 'a', 'd']

        if pos_x > 0 and pos_x <= linha:
            if pos_y > 0 and pos_y <= coluna:
                if direction in list_direction:
                    mapa, pontuacao, resp = lance(mapa, play, pontuacao, letrasJogaveis)
                    print(" ")
                    print(resp)
                else:
                    print(" ")
                    print("Jogada Irregular - Direção irregular")
            else:
                print(" ")
                print("Jogada Irregular - Coluna Irregular")
        else:
            print(" ")
            print("Jogada Irregular - Linha Irregular")

main()