import pygame
import random

pygame.init()

# Configurações da Janela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Pong')

# Cores (em Padrão RGB)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# --- Constantes do Jogo ---
LARGURA_RAQUETE = 15
ALTURA_RAQUETE = 100

VELOCIDADE_RAQUETE = 7

RAIO_BOLA = 10
VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_Y = 5

# Pontuacao
fonte_pontos = pygame.font.Font(None, 74) # Fonte padrão, tamanho 74



# --- Classes do Jogo ---
class Raquete:
    # O 'construtor': é chamado quando criamos uma Raquete
    # 'self' se refere ao próprio objeto
    def __init__(self, x, y):
        # O 'rect' armazena a posição (x,y) e o tamanho
        self.rect = pygame.Rect(x, y, LARGURA_RAQUETE, ALTURA_RAQUETE)

    # Método que ensina a raquete a se desenhar
    def desenhar(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect)
    
    def mover(self, tecla_cima, tecla_baixo):
        # Pega um "dicionário" de todas as teclas que estão pressionadas
        teclas = pygame.key.get_pressed()

        # Checa a tecla CIMA E se a raquete não saiu da tela
        if teclas[tecla_cima] and self.rect.top > 0:
            self.rect.y -= VELOCIDADE_RAQUETE
        # Checa a tecla BAIXO E se a raquete não saiu da tela
        if teclas[tecla_baixo] and self.rect.bottom < altura_tela:
            self.rect.y += VELOCIDADE_RAQUETE


class Bola:
    def __init__(self, x, y): # tem que ser 2 underline de cada lado do init pra definir o que vai acontecer
        self.rect = pygame.Rect(x - RAIO_BOLA, y - RAIO_BOLA, RAIO_BOLA * 2, RAIO_BOLA * 2)
        # Inicia com velocidade aleatória para X e Y
        self.vel_x = VELOCIDADE_BOLA_X * random.choice((1, -1)) # o choice escolhe aleatorio o comeco do jog
        self.vel_y = VELOCIDADE_BOLA_Y * random.choice((1, -1))

    def desenhar(self, tela):
        pygame.draw.ellipse(tela, BRANCO, self.rect) # Desenha um círculo

    def mover(self):
        # Atualiza a posição X e Y com base na velocidade
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    
    def verificar_colisao(self, raquete1, raquete2):
        # Colisão com paredes Cima/Baixo
        if self.rect.top <= 0 or self.rect.bottom >= altura_tela:
            self.vel_y *= -1 # Inverte a direção Y

        # Colisão com raquetes
        # 'colliderect' verifica se dois retângulos se tocam
        if self.rect.colliderect(raquete1) or self.rect.colliderect(raquete2):
            self.vel_x *= -1 # Inverte a direção X

       

    def resetar(self):
        # Move a bola de volta ao centro
        self.rect.x = largura_tela / 2 - RAIO_BOLA
        self.rect.y = altura_tela / 2 - RAIO_BOLA
        # Inverte a direção (para quem pontuou sacar) e dá uma pausa
        self.vel_x *= -1
        self.vel_y = VELOCIDADE_BOLA_Y * random.choice((1, -1))
        pygame.time.delay(1000) # Pausa por 1 seg

# --- Objetos do Jogo ---
# Cria a raquete1 a partir da classe Raquete
# Posição: 10 pixels da esquerda, e centralizada na altura
raquete1 = Raquete(10, altura_tela / 2 - ALTURA_RAQUETE / 2)

# Posição: 10 pixels da direita, e centralizado
raquete2 = Raquete(largura_tela - LARGURA_RAQUETE - 10, altura_tela / 2 - ALTURA_RAQUETE / 2)

bola = Bola(largura_tela / 2, altura_tela / 2)

pontos_1 = 0
pontos_2 = 0


# Prepara o relógio para controlar o FPS
relogio = pygame.time.Clock()

rodando = True
while rodando:
    # --- 1. Eventos ---
    # Verifica se o usuário fez alguma coisa
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Se clicou no "X"
            rodando = False

    # --- 2. Desenho ---
    # Limpa a tela pintando de preto
    tela.fill(PRETO)
 
   
    raquete1.desenhar(tela)
    raquete2.desenhar(tela)
    bola.desenhar(tela)

    #  Desenhar Placar ---
    # Linha central
    pygame.draw.aaline(tela, BRANCO, (largura_tela/2, 0), (largura_tela/2, altura_tela))

    # Placar Jogador 1 (esquerda)
    texto_p1 = fonte_pontos.render(str(pontos_1), True, BRANCO)
    tela.blit(texto_p1, (largura_tela/4, 20))

    # Placar Jogador 2 (direita)
    texto_p2 = fonte_pontos.render(str(pontos_2), True, BRANCO)
    tela.blit(texto_p2, (largura_tela * 3/4 - texto_p2.get_width(), 20))

    raquete1.mover(pygame.K_w, pygame.K_s)
    raquete2.mover(pygame.K_UP, pygame.K_DOWN)
    bola.mover()

    bola.verificar_colisao(raquete1.rect, raquete2.rect)
    if bola.rect.left < 0: # Bola saiu pela esquerda
            pontos_2 += 1
            bola.resetar()
    if bola.rect.right > largura_tela: # Bola saiu pela direita
            pontos_1 += 1
            bola.resetar()    
    



    # --- 3. Atualização da Tela ---
    # Mostra o que foi desenhado na tela
    pygame.display.flip()
    # Limita o jogo a 60 "frames" por segundo (FPS)
    relogio.tick(60)

pygame.quit()