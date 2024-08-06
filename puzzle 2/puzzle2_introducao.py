import pygame
from puzzle2_desafio import Puzzle_2
from puzzle2_coleta import comecar_coleta 

# Inicializa o Pygame:
pygame.init()

# Define a tela com o seu respectivo tamanho:
tela = pygame.display.set_mode((1280, 720))

# Define um nome pro jogo (aparece no canto superior da tela):
pygame.display.set_caption('Operação Crachá Perdido: Uma Aventura nos Centros da UFPE')
jogo = Puzzle_2()
# Variáveis para carregar a cena inicial da fase:
cena = pygame.image.load('puzzle 2/graphics/introducao-1.png')  # Coleta a cena inicial
cena = pygame.transform.scale(cena, (1280, 720))  # Ajusta a imagem para cobrir a tela inteira
aux_cena = 1  # Variável auxiliar para determinar qual a cena que está sendo exibida

# Seta a visualização da tela como sendo a imagem da cena:
tela.blit(cena, (0, 0))

# Define e executa a música de fundo em um loop infinito:
pygame.mixer.music.load('puzzle 2/sounds/Pokemon FireRedLeafGreen- Pokemon Center.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)


# Atualiza o display inicial do jogo:
pygame.display.flip()

# ----- Declarações de funções: -----

# Funcao do dialogo da introducao:
def animacao_incial():
    for n in range(4):
        if n == 0:
            cena = pygame.image.load('puzzle 2/graphics/introducao-2.png')
            pygame.time.wait(200)
        elif n == 1:
            cena = pygame.image.load('puzzle 2/graphics/introducao-3.png')
            pygame.time.wait(200)
        elif n == 2:
            cena = pygame.image.load('puzzle 2/graphics/introducao-4.png')
            pygame.time.wait(200)
        elif n == 3:
            cena = pygame.image.load('puzzle 2/graphics/introducao-5.png')
            pygame.time.wait(200)
        cena = pygame.transform.scale(cena, (1280, 720))
        tela.blit(cena, (0, 0))
        pygame.display.flip()

# Função para alterar a cena de acordo com a cena atual:

def alterar_cena():
    global aux_cena # Chama a variável global da cena auxiliar
    global status_jogo # Chama a variável global do status_jogo (cenas introdutórias)
    if aux_cena == 1: 
        animacao_incial()
        cena = pygame.image.load('puzzle 2/graphics/introducao-6.png')
    elif aux_cena == 2:
        cena = pygame.image.load('puzzle 2/graphics/introducao-7.png')
    elif aux_cena == 3:
        cena = pygame.image.load('puzzle 2/graphics/introducao-8.png')
    elif aux_cena == 4:
        cena = pygame.image.load('puzzle 2/graphics/introducao-9.png')
    elif aux_cena == 5:
        cena = pygame.image.load('puzzle 2/graphics/introducao-10.png')
    elif aux_cena == 6:
        cena = pygame.image.load('puzzle 2/graphics/introducao-11.png')
    elif aux_cena == 7:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load('puzzle 2/sounds/Pokemon RubySapphireEmerald- Pokemon Center.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        jogo.loop()    
        comecar_coleta()
    elif aux_cena == 8:
        #AQUI CHAMA O PROXIMO PUZZLE (combate)
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