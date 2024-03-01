class JogodaVelha:
    def __init__(self):
        self.tabuleiro = [['|___|', '|___|', '|___|'],
                          ['|___|', '|___|', '|___|'],
                          ['|___|', '|___|', '|___|']]
        self.jogadas = 0

    def jogador_atual(self):
        if self.jogadas in (1, 3, 5, 7, 9):
            return '| X |'
        else:
            return '| O |'
    
    def escolher_jogada(self, x, y):
        if self.tabuleiro[x][y] != '| X |' and self.tabuleiro[x][y] != '| O |':
            self.jogadas += 1
            self.tabuleiro[x][y] = self.jogador_atual()
        else:
            print('Já tem uma peça nessa posição! Digite novamente.')

    def show_status(self):
        print('-- Jogo Atual --')
        for i in range(0, 3):
            for j in range(0, 3):
                print(self.tabuleiro[i][j], end="")
            print('')

    def verifica_jogo(self):
        if self.jogadas >= 5:
            # Linhas
            if (self.tabuleiro[0][0] + self.tabuleiro[0][1] + self.tabuleiro[0][2] in ('| X || X || X |',
                                                                                       '| O || O || O |')):
                print('-- FIM DE JOGO --')
                return True
            elif (self.tabuleiro[1][0] + self.tabuleiro[1][1] + self.tabuleiro[1][2] in ('| X || X || X |',
                                                                                         '| O || O || O |')):
                print('-- FIM DE JOGO --')
                return True
            elif (self.tabuleiro[2][0] + self.tabuleiro[2][1] + self.tabuleiro[2][2] in ('| X || X || X |',
                                                                                         '| O || O || O |')):
                print('-- FIM DE JOGO --')
                return True
            # Colunas
            elif self.tabuleiro[0][0] + self.tabuleiro[1][0] + self.tabuleiro[2][0]:
                print('-- FIM DE JOGO --')
                return True
            elif self.tabuleiro[0][1] + self.tabuleiro[1][1] + self.tabuleiro[2][1]:
                print('-- FIM DE JOGO --')
                return True
            elif self.tabuleiro[0][2] + self.tabuleiro[1][2] + self.tabuleiro[2][2]:
                print('-- FIM DE JOGO --')
                return True
            # Diagonais
            elif self.tabuleiro[0][0] + self.tabuleiro[1][1] + self.tabuleiro[2][2]:
                print('-- FIM DE JOGO --')
                return True
            elif self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0]:
                print('-- FIM DE JOGO --')
                return True


jogo = JogodaVelha() 

while not jogo.verifica_jogo():
    jogo.show_status()
    x, y = input('Digite a linha e coluna desejada (0 - 2):').split()
    x = int(x)
    y = int(y)
    jogo.escolher_jogada(x, y)

jogo.show_status()

    
        