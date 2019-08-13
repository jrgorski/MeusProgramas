from IPython.display import clear_output

# Jogo da Velha
tabuleiro = [' '] * 10

#impressao do tabuleiro
def imprime_tabuleiro(tabuleiro):
    clear_output()
    print(tabuleiro[1] + "|" + tabuleiro[2] + "|" + tabuleiro[3])
    print("------")
    print(tabuleiro[4] + "|" + tabuleiro[5] + "|" + tabuleiro[6])
    print("------")
    print(tabuleiro[7] + "|" + tabuleiro[8] + "|" + tabuleiro[9])
    print("------")
#--------------------------------------------------------------------
# grava a jogada 
def jogada(jogador):
    posicao_casa = ' '
    while posicao_casa not in '1 2 3 4 5 6 7 8 9'.split(): 
        posicao_casa = input("Escolha sua jogada: (1-9):  " + jogador + ":")
        if posicao_casa in '1 2 3 4 5 6 7 8 9 0':
            return int(posicao_casa)
        else:
            print("Número Inválido")
#--------------------------------------------------------------------
       
#testa se a casa já esta preenchida
def testa_casaok(posicao_casa):
    if tabuleiro[posicao_casa] == "X" or tabuleiro[posicao_casa] == "O":
        print("posição já usada, use outra casa entre 1 a 9")
        return(False)
    else:
        return(True)
#--------------------------------------------------------------------
#Teste se ganhou        
def ganhou(marca):
        
    return((tabuleiro[1] == marca and tabuleiro[2] == marca and tabuleiro[3] == marca) or
           (tabuleiro[4] == marca and tabuleiro[5] == marca and tabuleiro[6] == marca) or
           (tabuleiro[7] == marca and tabuleiro[8] == marca and tabuleiro[9] == marca) or
           (tabuleiro[1] == marca and tabuleiro[5] == marca and tabuleiro[9] == marca) or
           (tabuleiro[1] == marca and tabuleiro[4] == marca and tabuleiro[7] == marca) or
           (tabuleiro[2] == marca and tabuleiro[5] == marca and tabuleiro[8] == marca) or
           (tabuleiro[3] == marca and tabuleiro[6] == marca and tabuleiro[9] == marca))
#--------------------------------------------------------------------        

#Programa principal
posicao_casa = 1
play1 = True
clear_output()
while posicao_casa != 0:
    
    if play1:
        posicao_casa = jogada("Jogador 1")

        if testa_casaok(posicao_casa):
            tabuleiro[posicao_casa] = "X"
            imprime_tabuleiro(tabuleiro)

            if ganhou("X"):
                posicao_casa = 0
                print("VIVA Jogador 1 Ganhou!!")
            play1 = False
    else:
        posicao_casa = jogada("Jogador 2")

        if testa_casaok(posicao_casa):
            tabuleiro[posicao_casa] = "O"
            imprime_tabuleiro(tabuleiro)

            if ganhou("O"):
                posicao_casa = 0
                print("VIVA Jogador 2 Ganhou!!")
            play1 = True
    

 
