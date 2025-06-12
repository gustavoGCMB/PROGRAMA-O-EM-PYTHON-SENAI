# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS 
# O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 

#O que acontece no jogo:
#Mostra um labirinto feito com blocos pretos e brancos.
#Temos que controlar um bloco vermelho,usando as setas do teclado.
#O jogador não pode atravessar as paredes.
#O jogo fecha quando o jogador clica no “X” da janela.
#O labirinto não tem saída.

#Como funciona:
#Inicia o Pygame e entra no jogo .
#A largura e altura do jogo é de 400,400.
#o código gera o labirinto e o jogador na tela.


#LABIRINTO (JOGO):

import pygame
pygame.init()
largura, altura = 400, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Labirinto")
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
tamanho_celula = 40
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
x, y = 1 * tamanho_celula, 1 * tamanho_celula
velocidade = 40
def desenhar_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
clock = pygame.time.Clock()
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    elif teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    elif teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    elif teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    tela.fill(branco)
    desenhar_labirinto()
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
