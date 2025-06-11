#circulo
import pygame

# Inicializar o pygame
pygame.init()

# Definir as dimensões da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Círculo com Pygame')

# Definir a cor do círculo (R, G, B)
cor_circulo = (255, 0, 0)  # Vermelho

# Definir a posição e o tamanho do círculo
posicao = (largura // 2, altura // 2)
raio = 50

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Preencher a tela com cor branca
    tela.fill((255, 255, 255))

    # Desenhar o círculo
    pygame.draw.circle(tela, cor_circulo, posicao, raio)

    # Atualizar a tela
    pygame.display.update()

# Fechar o pygame
pygame.quit()


# elipse
import pygame

# Inicializar o pygame
pygame.init()

# Definir as dimensões da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Elipse com Pygame')

# Definir a cor da elipse (R, G, B)
cor_elipse = (0, 255, 0)  # Verde

# Definir a posição e o tamanho da elipse
posicao = (largura // 2 - 100, altura // 2 - 50)  # Posição superior esquerda da caixa delimitadora
tamanho = (200, 100)  # Largura e altura da elipse

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Preencher a tela com cor branca
    tela.fill((255, 255, 255))

    # Desenhar a elipse
    pygame.draw.ellipse(tela, cor_elipse, pygame.Rect(posicao, tamanho))

    # Atualizar a tela
    pygame.display.update()

# Fechar o pygame
pygame.quit()