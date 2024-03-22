from jogo_da_velha_controller import JogodaVelha


def main():
    jogo = JogodaVelha()
    while not jogo.verifica_jogo():
        jogo.show_status()
        x, y = input('Digite a linha e coluna desejada (0 - 2):').split()
        x = int(x)
        y = int(y)
        if x > 2 or y > 2:
            print("Digite uma coordenada válida, entre 0 e 2")
            continue
        jogo.escolher_jogada(x, y)
    jogo.show_status()


if __name__ == '__main__':
    main()

    
        