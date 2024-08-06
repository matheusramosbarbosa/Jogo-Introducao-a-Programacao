import pygame
import puzzle_2 as p2

# Inicializa o Pygame:
pygame.init()

# Define a tela com o seu respectivo tamanho:
tela = pygame.display.set_mode((1280, 720))

# Define um nome pro jogo (aparece no canto superior da tela):
pygame.display.set_caption('Operação Crachá Perdido: Uma Aventura nos Centros da UFPE')

# Variáveis para carregar a cena inicial da fase:
cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena1.png')  # Coleta a cena inicial
cena = pygame.transform.scale(cena, (1280, 720))  # Ajusta a imagem para cobrir a tela inteira
aux_cena = 1  # Variável auxiliar para determinar qual a cena que está sendo exibida

# Seta a visualização da tela como sendo a imagem da cena:
tela.blit(cena, (0, 0))

# Define e executa a música de fundo em um loop infinito:
pygame.mixer.music.load('sons-puzzle1/som-musica-fundo.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.8)

# Atualiza o display inicial do jogo:
pygame.display.flip()

# ----- Declarações de funções: -----

# Função para alterar a cena de acordo com a cena atual:
def alterar_cena():
    global aux_cena # Chama a variável global da cena auxiliar
    global status_jogo # Chama a variável global do status_jogo (cenas introdutórias)

    # Se a cena atual for a 1, então carrega o segundo cenário e assim sucessivamente:
    if aux_cena == 1:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena2.png')
    elif aux_cena == 2:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena3.png')
    elif aux_cena == 3:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena4.png')
    elif aux_cena == 4:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena5.png')
    elif aux_cena == 5:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena6.png')
    elif aux_cena == 6:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena7.png')
    elif aux_cena == 7:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena8.png')
    elif aux_cena == 8:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena9.png')
    elif aux_cena == 9:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena10.png')
    elif aux_cena == 10:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena11.png')
    elif aux_cena == 11:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena12.png')
    elif aux_cena == 12:
        cena = pygame.image.load('imagens-puzzle1/cenas-introducao/puzzle1-cena13.png')
    elif aux_cena == 13:
        p2.Puzzle_2.loop() # Começa a disputa de penâltis
    elif aux_cena == 14:
        status_jogo = False # Encerra o loop infinito

    cena = pygame.transform.scale(cena, (1280, 720))
    tela.blit(cena, (0, 0))
    pygame.display.flip()
    aux_cena += 1

# ----- Execução do jogo: -----

#Variável para definir se o jogo está sendo executado (se True). Se False, é devido ao jogador ter fechado a tela:
status_jogo = True

#Executa um loop infinito para rodar o jogo, até que saia da tela:
while status_jogo:

    # Executa um loop percorrendo as ações realizadas no jogo:
    for event in pygame.event.get():
        # Se a ação realizada for clicar no botão de fechar a tela, sai do jogo:
        if event.type == pygame.QUIT:
            status_jogo = False
        # Se ação realizada for clicar em uma tecla:
        elif event.type == pygame.KEYDOWN:
            # Se a tecla for o ENTER, chama a função de alterar a cena do jogo:
            if event.key == pygame.K_SPACE:
                alterar_cena()