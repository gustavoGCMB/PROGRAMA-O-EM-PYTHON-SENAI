import pygame

pygame.init()
tamanho = 500, 500
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption('jogo pin - pong')

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Posições iniciais
raquete1_x, raquete1_y = 50, 225
raquete2_x, raquete2_y = 430, 225
ball_x, ball_y = 250, 250
velocidade_bola_x = 2
velocidade_bola_y = 2
velocidade_raquete = 4

# Tamanhos
raquete_altura, largura_raquete = 100, 10
bola_largura, bola_altura = 20, 20

# Placar
placar1 = 0
placar2 = 0
font = pygame.font.SysFont(None, 55)

# Loop principal
LOOP = True
clock = pygame.time.Clock()

while LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            LOOP = False

    # Movimentos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete1_y < 500 - raquete_altura:
        raquete1_y += velocidade_raquete
    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < 500 - raquete_altura:
        raquete2_y += velocidade_raquete

    # Movimento da bola
    ball_x += velocidade_bola_x
    ball_y += velocidade_bola_y

    # Colisão com topo e base
    if ball_y <= 0 or ball_y + bola_altura >= 500:
        velocidade_bola_y = -velocidade_bola_y

    # Colisão com raquetes
    if (raquete1_x < ball_x < raquete1_x + largura_raquete) and (raquete1_y < ball_y < raquete1_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x
    if (raquete2_x < ball_x + bola_largura < raquete2_x + largura_raquete) and (raquete2_y < ball_y < raquete2_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x

    # Pontuação
    if ball_x < 0:
        placar2 += 1
        ball_x, ball_y = 250, 250
    if ball_x > 500:
        placar1 += 1
        ball_x, ball_y = 250, 250

    # Desenhar tela
    tela.fill(BRANCO)
    pygame.draw.rect(tela, PRETO, (raquete1_x, raquete1_y, largura_raquete, raquete_altura))
    pygame.draw.rect(tela, PRETO, (raquete2_x, raquete2_y, largura_raquete, raquete_altura))
    pygame.draw.ellipse(tela, PRETO, (ball_x, ball_y, bola_largura, bola_altura))
    placar_texto = font.render(f'{placar1} | {placar2}', True, PRETO)
    tela.blit(placar_texto, (200, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
