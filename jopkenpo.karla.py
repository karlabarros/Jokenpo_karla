# Função choise fará o papel do computador
from random import choice

# Lista das jogadas válidas

play = ["pedra", "papel", "tesoura"]

# Matriz dos resultados possíveis, contendo as regras do jogo
rule = (("e", "d", "v"), ("v", "e", "d"), ("d", "v", "e"))

# Texto a ser exibido na tela para cada resultado possível
text = {
    "e": "    Deu empate! Tente novamente!",
    "v": "    Parabéns, você venceu!",
    "d": "    Você foi derrotado!",
}

# Jogo propriamente dito

while True:
    h, c = input("Faça a sua jogada - Pedra, Papel ou Tesoura: ").lower(), choice(play)

    if h == "sair":  # É sempre uma boa prática ter uma saída de um laço while True
        break

    if h in play:  # E um teste de que a jogada foi válida
        print(f"  O computador jogou {c}")
        print(text[rule[play.index(h)][play.index(c)]])
    else:
        print(f"  As jogadas válidas são:\n {play}")

