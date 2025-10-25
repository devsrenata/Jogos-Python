#  Baixar o Pygame o Importar o Pygame 

import pygame
import random #classe do python para fazer coisas aleatorias

# Inicia o Pygame
pygame.init()

pygame.mixer.init() # Coloca audio


#Variaveis Relevantes para o Jogo
ALTURA_TELA = 600
LARGURA_TELA = 800

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption ('Acerte o Alvo') 

# Cores
PRETO = (0,0,0)
BRANCO =(255, 255, 255)
VERMELHO = (255, 0, 0)

relogio = pygame.time.Clock()
rodando = True

# Formato do retangulo / TAMANHO
TAMANHO_ALVO = 50
                    # Onde vai aparecer na tela / tamanho do objeto  #larg  #altura
alvo_rect = pygame.Rect(375, 275, TAMANHO_ALVO, TAMANHO_ALVO) # Esse rect permite que desenhe um retangulo na tela

pontuacao = 0

fonte = pygame.font.SysFont("bahnschrift", 35)

som_acerto = pygame.mixer.Sound("acerto.wav")   # variavel do audio

while rodando:
    # 1. Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # QUIT FECHA O JOGO ele e o evento quando clica no x
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN: # Evento de click no quadrado
            if alvo_rect.collidepoint(evento.pos): # clicou no retangulo / event.pos = posicao do retangulo           
                # Calcula uma nova posição X aleatória
                alvo_rect.x = random.randrange(0, LARGURA_TELA - TAMANHO_ALVO)
                # Calcula uma nova posição Y aleatória
                alvo_rect.y = random.randrange(0, ALTURA_TELA - TAMANHO_ALVO)
                pontuacao += 1 
                som_acerto.play() # Chamando o audio



    tela.fill(PRETO) # fill preecnhe atela preta     
    pygame.draw.rect(tela, VERMELHO, alvo_rect)
    texto_pontos = fonte.render(f"Pontos: {pontuacao}" , True, BRANCO) 
    tela.blit(texto_pontos, (10,10)) #  blit Mostra o texto que virou imagem
    pygame.display.flip()   # quando coloca o flip mostra na tela
    relogio.tick(60)

pygame.quit() # Esse quit encerra o Pygame