import pygame

def avancar_cena():
    pygame.init()

    tela = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Operação Crachá Perdido: Uma Aventura nos Centros da UFPE')
    #icone = pygame.image.load('imagens-puzzle1/cenas-introducao/icone_ocp.png')
    #pygame.display.set_icon(icone)
    cena = pygame.image.load('imagens-puzzle1/cenas-coleta/provisorio-continua.png')
    cena = pygame.transform.scale(cena, (1280, 720))
    tela.blit(cena, (0, 0))
    pygame.display.flip()

    status_fase2 = True
    while status_fase2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status_fase2 = False