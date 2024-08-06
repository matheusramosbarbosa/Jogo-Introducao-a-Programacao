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
cena = pygame.image.load('puzzle 2/graphics/fase_1.png')  # Coleta a cena inicial
cena = pygame.transform.scale(cena, (1280, 720))  # Ajusta a imagem para cobrir a tela inteira
aux_cena = 1  # Variável auxiliar para determinar qual a cena que está sendo exibida

# Seta a visualização da tela como sendo a imagem da cena:
tela.blit(cena, (0, 0))

# Define e executa a música de fundo em um loop infinito:
pygame.mixer.music.load('puzzle 2/sounds/Pokemon FireRedLeafGreen- Pokemon Center.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)


# Atualiza o display inicial do jogo:
pygame.display.flip()

# ----- Declarações de funções: -----

# Funcao do dialogo da introducao:
def dialogo_introducao():
    qualquercoisa = True

# Função para alterar a cena de acordo com a cena atual:

def alterar_cena():
    global aux_cena # Chama a variável global da cena auxiliar
    global status_jogo # Chama a variável global do status_jogo (cenas introdutórias)
    if aux_cena == 1:
        dialogo_introducao()
    if aux_cena == 2:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load('puzzle 2/sounds/Pokemon RubySapphireEmerald- Pokemon Center.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        jogo.loop()    
        alterar_cena()
        
    elif aux_cena == 3:
        comecar_coleta()

        #AQUI CHAMA O PROXIMO PUZZLE (combate)
        status_jogo = False # Encerra o loop infinito

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