import pygame
from random import randint
from puzzle1_coleta import comecar_coleta
from objetos_personagem import Infos_Coletaveis
from objetos_personagem import infos_coletaveis

# Inicializa o Pygame:
pygame.init()

# Define a tela com o seu respectivo tamanho:
tela = pygame.display.set_mode((1280, 720))

# Coleta as logos dos competidores e redimensiona:
logo_robocin = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/logo-robocin.png')
logo_robocin = pygame.transform.scale(logo_robocin, (80, 80))
logo_voxarlabs = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/logo-voxarlabs.png')
logo_voxarlabs = pygame.transform.scale(logo_voxarlabs, (80, 80))

# Criação de uma variável auxiliar para verificar de quem é a fez de chutar e, consequentemente, de quem defender:
vez_chute = 'robocin' # No início, o RobôCIn começa chutando

# Criação de variáveis do placar da partida:
pontos_robocin = 0
pontos_voxar = 0

# Coleta a fonte do placar durante as rodadas e o resultado final:
fonte = pygame.font.SysFont('freesansbold.ttf', 50) #Coleta a fonte a ser utilizada no placar durante as rodadas
fonte_final = pygame.font.SysFont('freesansbold.ttf', 100) #Coleta a fonte a ser utilizada no placar do resultado final

# ----- Declarações de funções: -----

# Função para desenhar um botão:
def desenhar_botao(cena, cor, posicao_x, posicao_y, largura, altura, texto):
    pygame.draw.rect(cena, cor, (posicao_x, posicao_y, largura, altura)) #Desenha um retângulo
    font = pygame.font.Font(None, 36) #Determina uma fonte
    texto_superficie = font.render(texto, True, (0, 0, 0)) #Coleta um texto pra ficar na superfície da tela
    text_rect = texto_superficie.get_rect(center = (posicao_x + largura // 2, posicao_y + altura // 2)) #Coleta o texto do retângulo
    cena.blit(texto_superficie, text_rect) #Exibe os textos na cena

# Função para desenhar um texto:
def desenhar_placar(cena, texto, fonte, cor, x, y):
    texto_superficie = fonte.render(texto, True, cor)
    texto_rect = texto_superficie.get_rect()
    texto_rect.topleft = (x, y)
    cena.blit(texto_superficie, texto_rect)

# Função para redimensionar e exibir a cena:
def exibir_cena(cena):
    cena = pygame.transform.scale(cena, (1280, 720)) # Ajusta a imagem para cobrir a tela inteira
    cena.blit(logo_robocin, (50, 590)) # Exibe a logo do RobôCIn
    cena.blit(logo_voxarlabs, (1150, 590)) # Exibe a logo do Voxar Labs
    desenhar_placar(cena, str(pontos_robocin), fonte, (255, 255, 255), 150, 615)
    desenhar_placar(cena, str(pontos_voxar), fonte, (255, 255, 255), 1120, 615)
    tela.blit(cena, (0, 0)) # Seta a visualização da tela como sendo a imagem da cena
    visualizar_infos_coletaveis()
    pygame.display.flip() # Atualiza o display inicial do puzzle1

# Função para passar a cena em caso de ponto do RobôCIn:
def passar_ponto_robocin():
    global pontos_robocin

    som_acerto = pygame.mixer.Sound('puzzle1/sons-puzzle1/puzzle1-som-acerto.mp3')
    som_acerto.play()
    pygame.time.wait(2900) # Tempo para ouvir as vaias
    pontos_robocin += 1
    passar_cena_ponto()

# Função para passar a cena em caso de ponto do Voxar Labs:
def passar_ponto_voxar():
    global pontos_voxar

    som_erro = pygame.mixer.Sound('puzzle1/sons-puzzle1/puzzle1-som-erro.mp3')
    som_erro.play()
    pygame.time.wait(2300) # Tempo para ouvir a comemoração
    pontos_voxar += 1
    passar_cena_ponto()

# Função para passar a cena após a marcação de ponto de alguma equipe:
def passar_cena_ponto():
    global vez_chute, pontos_robocin, pontos_voxar

    # Se ainda não houver tido as 5 rodadas da disputa:
    if (pontos_robocin + pontos_voxar) < 5:
        if vez_chute == 'robocin':
            vez_chute = 'voxarlabs'
            partida_defesa()

        elif vez_chute == 'voxarlabs':
            vez_chute = 'robocin'
            partida_chute()

    # Se a disputa de penâltis tiver chegado ao fim:
    else:
        # Se o RobôCIn venceu:
        if pontos_robocin > pontos_voxar:
            exibir_resultado_final('robocin')

        # Se o Voxar Labs venceu:
        elif pontos_voxar > pontos_robocin:
            exibir_resultado_final('voxarlabs')

# Função chamada pela introdução, para iniciar a partida:
def comecar_partida():
    # Estabelece e executa a música de fundo:
    pygame.mixer.music.load('puzzle1/sons-puzzle1/puzzle1-som-torcida-fundo.mp3')
    pygame.mixer.music.set_volume(4)
    pygame.mixer.music.play(-1)  # -1 faz com que a música toque em loop

    partida_chute() # Começa a disputa de penâltis

# Função para exibir o resultado final de acordo com o vencedor:
def exibir_resultado_final(vencedor):
    global pontos_robocin, pontos_voxar

    if vencedor == 'robocin':
        cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VITORIA-ROBOCIN.png')
        cena = pygame.transform.scale(cena, (1280, 720))
        desenhar_placar(cena, str(pontos_robocin), fonte_final, (255, 255, 255), 250, 330)
        desenhar_placar(cena, str(pontos_voxar), fonte_final, (255, 255, 255), 980, 330)
        tela.blit(cena, (0, 0))
        pygame.display.flip()

    elif vencedor == 'voxarlabs':
        cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VITORIA-VOXARLABS.png')
        cena = pygame.transform.scale(cena, (1280, 720))
        desenhar_placar(cena, str(pontos_robocin), fonte_final, (255, 255, 255), 250, 330)
        desenhar_placar(cena, str(pontos_voxar), fonte_final, (255, 255, 255), 980, 330)
        tela.blit(cena, (0, 0))
        pygame.display.flip()

    # Bloco para apenas mudar de cena caso aperte espaço:
    status_resultado = True
    while status_resultado:
        visualizar_infos_coletaveis()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status_resultado = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if vencedor == 'robocin':
                        comecar_coleta()

                    elif vencedor == 'voxarlabs':
                        pontos_robocin, pontos_voxar = 0, 0
                        comecar_partida()
                        status_resultado = False

# Função para realizar a jogada da máquina:
def jogada_maquina():
    #Coleta uma jogada aleatória da máquina:
    num_jogada = randint(1, 2)

    #Se o número da jogada for 1, a jogada será para a esquerda e assim segue:
    if num_jogada == 1:
        return 'esquerda'
    elif num_jogada == 2:
        return 'centro'
    elif num_jogada == 3:
        return 'direita'

# Função para chutar na partida (disputa de penâltis):
def partida_chute():
    # Reproduz o som do apito, indicando o início da rodada:
    som_apito = pygame.mixer.Sound('puzzle1/sons-puzzle1/puzzle1-som-apito.mp3')
    som_apito.set_volume(0.3)
    som_apito.play()

    # Exibe a cena e as informações de placar, etc:
    cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCINvsVOXAR.png')
    cena = pygame.transform.scale(cena, (1280, 720))
    cena.blit(logo_robocin, (50, 590))
    cena.blit(logo_voxarlabs, (1150, 590))
    desenhar_placar(cena, str(pontos_robocin), fonte, (255, 255, 255), 150, 615)
    desenhar_placar(cena, str(pontos_voxar), fonte, (255, 255, 255), 1120, 615)
    tela.blit(cena, (0, 0))
    visualizar_infos_coletaveis()
    pygame.display.flip()
    #Obs.: Aqui não usa a função exibir_cena() pois é o primeiro carregamento de tela do chute

    # Cria os botões de seleção:
    botao_esquerda = pygame.Rect(250, 600, 200, 50)
    botao_centro = pygame.Rect(550, 600, 200, 50)
    botao_direita = pygame.Rect(850, 600, 200, 50)

    # Desenha os botões e exibe na tela:
    tela.blit(cena, (0, 0))
    desenhar_botao(tela, (51, 255, 255), botao_esquerda.x, botao_esquerda.y, botao_esquerda.width, botao_esquerda.height, 'Esquerda')
    desenhar_botao(tela, (51, 255, 255), botao_centro.x, botao_centro.y, botao_centro.width, botao_centro.height,'Centro')
    desenhar_botao(tela, (51, 255, 255), botao_direita.x, botao_direita.y, botao_direita.width, botao_direita.height,'Direita')

    visualizar_infos_coletaveis()
    pygame.display.flip()

    # Tempo para ouvir o apito:
    pygame.time.wait(1000)

    # Variável para definir se a partida está sendo acontecendo (se True). Se False, é devido ao jogador ter terminado:
    status_partida = True

    # Executa um loop infinito para executar a partida:
    while status_partida:

        # Executa um loop percorrendo as ações realizadas no puzzle1:
        for event in pygame.event.get():
            # Se a ação realizada for clicar no botão de fechar a tela, sai do puzzle1:
            if event.type == pygame.QUIT:
                status_partida = False

            # Se a ação realizada for clicar em um botão do mouse:
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos #Coleta o clique

                # Coleta pra onde é o chute de acordo com o botão pressionado:
                if botao_esquerda.collidepoint(mouse_x, mouse_y):
                    chute_robocin = 'esquerda'

                elif botao_centro.collidepoint(mouse_x, mouse_y):
                    chute_robocin = 'centro'

                elif botao_direita.collidepoint(mouse_x, mouse_y):
                    chute_robocin = 'direita'

                # Coleta o lado da defesa do Voxar:
                defesa_voxar = jogada_maquina()

                # Verifica se o jogador clicou em um botão. Se não clicou, elogia ele:
                try:
                    # Efetua a jogada de acordo com o chute do RobôCIn e a defesa do Voxar Labs:
                    efetuar_jogada(chute_robocin, defesa_voxar)
                    status_partida = False
                except UnboundLocalError:
                    print('Clica em um botão, cara de percata!')

# Função para defender na partida (disputa de penâltis):
def partida_defesa():
    # Reproduz o som do apito, indicando o início da rodada:
    som_apito = pygame.mixer.Sound('puzzle1/sons-puzzle1/puzzle1-som-apito.mp3')
    som_apito.play()

    # Exibe a cena e as informações de placar, etc:
    cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXARvsROBOCIN.png')
    cena = pygame.transform.scale(cena, (1280, 720))
    cena.blit(logo_robocin, (50, 590))
    cena.blit(logo_voxarlabs, (1150, 590))
    desenhar_placar(cena, str(pontos_robocin), fonte, (255, 255, 255), 150, 615)
    desenhar_placar(cena, str(pontos_voxar), fonte, (255, 255, 255), 1120, 615)
    tela.blit(cena, (0, 0))
    visualizar_infos_coletaveis()
    pygame.display.flip()
    # Obs.: Aqui não usa a função exibir_cena() pois é o primeiro carregamento de tela da defesa

    # Cria os botões de seleção:
    botao_esquerda = pygame.Rect(250, 600, 200, 50)
    botao_centro = pygame.Rect(550, 600, 200, 50)
    botao_direita = pygame.Rect(850, 600, 200, 50)

    # Desenha os botões e exibe na tela:
    tela.blit(cena, (0, 0))
    desenhar_botao(tela, (51, 255, 255), botao_esquerda.x, botao_esquerda.y, botao_esquerda.width,botao_esquerda.height, 'Esquerda')
    desenhar_botao(tela, (51, 255, 255), botao_centro.x, botao_centro.y, botao_centro.width, botao_centro.height,'Centro')
    desenhar_botao(tela, (51, 255, 255), botao_direita.x, botao_direita.y, botao_direita.width, botao_direita.height,'Direita')
    visualizar_infos_coletaveis()
    pygame.display.flip()

    # Tempo para ouvir o apito:
    pygame.time.wait(1000)

    # Variável para definir se a partida está sendo acontecendo (se True). Se False, é devido ao jogador ter terminado:
    status_partida = True

    # Executa um loop infinito para executar a partida:
    while status_partida:

        # Executa um loop percorrendo as ações realizadas no puzzle1:
        for event in pygame.event.get():
            # Se a ação realizada for clicar no botão de fechar a tela, sai do puzzle1:
            if event.type == pygame.QUIT:
                status_partida = False

            # Se a ação realizada for clicar em um botão do mouse:
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos  # Coleta o clique

                # Coleta pra onde é o chute de acordo com o botão pressionado:
                if botao_esquerda.collidepoint(mouse_x, mouse_y):
                    defesa_robocin = 'esquerda'

                elif botao_centro.collidepoint(mouse_x, mouse_y):
                    defesa_robocin = 'centro'

                elif botao_direita.collidepoint(mouse_x, mouse_y):
                    defesa_robocin = 'direita'

                # Coleta o lado da defesa do Voxar:
                chute_voxarlabs = jogada_maquina()

                # Efetua a jogada de acordo com o chute do RobôCIn e a defesa do Voxar Labs:
                efetuar_jogada(chute_voxarlabs, defesa_robocin)
                status_partida = False

# Função para efetuar a jogada (chute e defesa):
def efetuar_jogada(chute, defesa):
    # Chama as funções globais das pontuações e da vez do chute:
    global pontos_robocin, pontos_voxar, vez_chute

    #Se a vez do chute for do RobôCIn:
    if vez_chute == 'robocin':
        #Verifica o chute do RobôCIn e a defesa do Voxar Labs:
        if chute == 'centro' and defesa == 'centro':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-DEFENDE-CENTRO.png')
            exibir_cena(cena)
            passar_ponto_voxar()

        elif chute == 'esquerda' and defesa == 'centro':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-ESQUERDA-VOXAR-CENTRO.png')
            exibir_cena(cena)
            passar_ponto_robocin()

        elif chute == 'direita' and defesa == 'centro':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-DIREITA-VOXAR-CENTRO.png')
            exibir_cena(cena)
            passar_ponto_robocin()

        elif chute == 'direita' and defesa == 'direita':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-DEFENDE-DIREITA.png')
            exibir_cena(cena)
            passar_ponto_voxar()

        elif chute == 'centro' and defesa == 'direita':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-CENTRO-VOXAR-DIREITA.png')
            exibir_cena(cena)
            passar_ponto_robocin()

        elif chute == 'esquerda' and defesa == 'direita':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-ESQUERDA-VOXAR-DIREITA.png')
            exibir_cena(cena)
            passar_ponto_robocin()

        elif chute == 'esquerda' and defesa == 'esquerda':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-DEFENDE-ESQUERDA.png')
            exibir_cena(cena)
            passar_ponto_voxar()

        elif chute == 'centro' and defesa == 'esquerda':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-CENTRO-VOXAR-ESQUERDA.png')
            exibir_cena(cena)
            passar_ponto_robocin()

        elif chute == 'direita' and defesa == 'esquerda':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-DIREITA-VOXAR-ESQUERDA.png')
            exibir_cena(cena)
            passar_ponto_robocin()

    # Se a vez do chute for do Voxar Labs:
    elif vez_chute == 'voxarlabs':
        # Verifica o chute do Voxar Labs e a defesa do RobôCIn:
        if chute == 'centro' and defesa == 'centro':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-DEFENDE-CENTRO.png')
            exibir_cena(cena)
            passar_ponto_robocin()

        elif chute == 'esquerda' and defesa == 'centro':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-ESQUERDA-ROBOCIN-CENTRO.png')
            exibir_cena(cena)
            passar_ponto_voxar()

        elif chute == 'direita' and defesa == 'centro':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-DIREITA-ROBOCIN-CENTRO.png')
            exibir_cena(cena)
            passar_ponto_voxar()

        elif chute == 'direita' and defesa == 'direita':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-DEFENDE-DIREITA.png')
            exibir_cena(cena)
            passar_ponto_robocin()

        elif chute == 'centro' and defesa == 'direita':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-CENTRO-ROBOCIN-DIREITA.png')
            exibir_cena(cena)
            passar_ponto_voxar()

        elif chute == 'esquerda' and defesa == 'direita':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-ESQUERDA-ROBOCIN-DIREITA.png')
            exibir_cena(cena)
            passar_ponto_voxar()

        elif chute == 'esquerda' and defesa == 'esquerda':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-DEFENDE-ESQUERDA.png')
            exibir_cena(cena)
            passar_ponto_robocin()

        elif chute == 'centro' and defesa == 'esquerda':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-CENTRO-ROBOCIN-ESQUERDA.png')
            exibir_cena(cena)
            passar_ponto_voxar()

        elif chute == 'direita' and defesa == 'esquerda':
            cena = pygame.image.load('puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-DIREITA-ROBOCIN-ESQUERDA.png')
            exibir_cena(cena)
            passar_ponto_voxar()

# Exibe as informações dos coletáveis:
def visualizar_infos_coletaveis():
    view_infos_coletaveis = pygame.image.load('puzzle1/visualizacao_coletaveis.png')
    tela.blit(view_infos_coletaveis,(10,220))

    fonte = pygame.font.SysFont('freesansbold.ttf', 70)

    txt_info_cracha = fonte.render(str(infos_coletaveis.qtd_cracha), True, (255, 255, 255))
    tela.blit(txt_info_cracha, (80, 235))

    txt_info_fragmento_2 = fonte.render(str(infos_coletaveis.qtd_fragmento_2), True, (255, 255, 255))
    tela.blit(txt_info_fragmento_2, (80, 312))

    txt_info_fragmento_1 = fonte.render(str(infos_coletaveis.qtd_fragmento_1), True, (255, 255, 255))
    tela.blit(txt_info_fragmento_1, (80, 388))

    pygame.display.flip()