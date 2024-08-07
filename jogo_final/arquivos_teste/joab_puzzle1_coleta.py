import pygame

pygame.init()

tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Operação Crachá Perdido: Uma Aventura nos Centros da UFPE')

status_coleta = True

def comecar_coleta():
    cena = pygame.image.load('../puzzle1/imagens-puzzle1/personagem-coletavel-cena_coletavel/puzzle1-cena-coleta.png')
    cena = pygame.transform.scale(cena, (1280, 720))
    tela.blit(cena, (0, 0))
    pygame.display.flip()

    while status_coleta:
        print('em desenvolvimento. isso vai print infinito e não consegue fechar a tela até parar no pycharm/vscode :)')