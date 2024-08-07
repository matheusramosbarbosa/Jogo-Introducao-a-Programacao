import pygame
from random import randint
from arquivos_teste.joab_puzzle1_coleta import comecar_coleta

# Inicializa o Pygame:
pygame.init()

# Define a tela com o seu respectivo tamanho:
tela = pygame.display.set_mode((1280, 720))

# Coleta as logos dos competidores e redimensiona:
logo_robocin = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-partida/logo-robocin.png')
logo_robocin = pygame.transform.scale(logo_robocin, (80, 80))
logo_voxarlabs = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-partida/logo-voxarlabs.png')
logo_voxarlabs = pygame.transform.scale(logo_voxarlabs, (80, 80))

# Criação de uma variável auxiliar para verificar de quem é a fez de chutar e, consequentemente, de quem defender:
vez_chute = 'robocin' # No início, o RobôCIn começa chutando

# Criação de variáveis do placar da partida:
pontos_robocin = 0
pontos_voxar = 0

# Coleta a fonte do placar durante as rodadas e o resultado final:
fonte = pygame.font.SysFont('freesanbold.ttf', 50) #Coleta a fonte a ser utilizada no placar durante as rodadas
fonte_final = pygame.font.SysFont('freesanbold.ttf', 100) #Coleta a fonte a ser utilizada no placar do resultado final

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
    pygame.display.flip() # Atualiza o display inicial do puzzle1

# Função chamada pela introdução, para iniciar a partida:
def comecar_partida():
    partida_chute()

# Função para exibir o resultado final de acordo com o vencedor:
def exibir_resultado_final(vencedor):
    if vencedor == 'robocin':
        cena = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VITORIA-ROBOCIN.png')
        cena = pygame.transform.scale(cena, (1280, 720))
        desenhar_placar(cena, str(pontos_robocin), fonte_final, (255, 255, 255), 250, 330)
        desenhar_placar(cena, str(pontos_voxar), fonte_final, (255, 255, 255), 980, 330)
        tela.blit(cena, (0, 0))
        pygame.display.flip()

    elif vencedor == 'voxarlabs':
        cena = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VITORIA-VOXARLABS.png')
        cena = pygame.transform.scale(cena, (1280, 720))
        desenhar_placar(cena, str(pontos_robocin), fonte_final, (255, 255, 255), 250, 330)
        desenhar_placar(cena, str(pontos_voxar), fonte_final, (255, 255, 255), 980, 330)
        tela.blit(cena, (0, 0))
        pygame.display.flip()

# Função para realizar a jogada da máquina:
def jogada_maquina():
    #Coleta uma jogada aleatória da máquina:
    num_jogada = randint(1, 3)

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
    pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-apito.mp3')
    pygame.mixer.music.play()

    # Exibe a cena e as informações de placar, etc:
    cena = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCINvsVOXAR.png')
    cena = pygame.transform.scale(cena, (1280, 720))
    cena.blit(logo_robocin, (50, 590))
    cena.blit(logo_voxarlabs, (1150, 590))
    desenhar_placar(cena, str(pontos_robocin), fonte, (255, 255, 255), 150, 615)
    desenhar_placar(cena, str(pontos_voxar), fonte, (255, 255, 255), 1120, 615)
    tela.blit(cena, (0, 0))
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
    pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-apito.mp3')
    pygame.mixer.music.play()

    # Exibe a cena e as informações de placar, etc:
    cena = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXARvsROBOCIN.png')
    cena = pygame.transform.scale(cena, (1280, 720))
    cena.blit(logo_robocin, (50, 590))
    cena.blit(logo_voxarlabs, (1150, 590))
    desenhar_placar(cena, str(pontos_robocin), fonte, (255, 255, 255), 150, 615)
    desenhar_placar(cena, str(pontos_voxar), fonte, (255, 255, 255), 1120, 615)
    tela.blit(cena, (0, 0))
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
    global pontos_robocin
    global pontos_voxar
    global vez_chute

    #Se a vez do chute for do RobôCIn:
    if vez_chute == 'robocin':
        #Verifica o chute do RobôCIn e a defesa do Voxar Labs:
        if chute == 'centro' and defesa == 'centro':
            cena = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-DEFENDE-CENTRO.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-erro.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(900) # Tempo para ouvir as vaias
            pontos_voxar += 1

        elif chute == 'esquerda' and defesa == 'centro':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-ESQUERDA-VOXAR-CENTRO.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-acerto.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(3000) # Tempo para ouvir a comemoração
            pontos_robocin += 1

        elif chute == 'direita' and defesa == 'centro':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-DIREITA-VOXAR-CENTRO.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-acerto.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(3000) # Tempo para ouvir a comemoração
            pontos_robocin += 1

        elif chute == 'direita' and defesa == 'direita':
            cena = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-DEFENDE-DIREITA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-erro.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(900) # Tempo para ouvir as vaias
            pontos_voxar += 1

        elif chute == 'centro' and defesa == 'direita':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-CENTRO-VOXAR-DIREITA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-acerto.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(3000) # Tempo para ouvir a comemoração
            pontos_robocin += 1

        elif chute == 'esquerda' and defesa == 'direita':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-ESQUERDA-VOXAR-DIREITA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-acerto.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(3000) # Tempo para ouvir a comemoração
            pontos_robocin += 1

        elif chute == 'esquerda' and defesa == 'esquerda':
            cena = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-DEFENDE-ESQUERDA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-erro.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(900) # Tempo para ouvir as vaias
            pontos_voxar += 1

        elif chute == 'centro' and defesa == 'esquerda':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-CENTRO-VOXAR-ESQUERDA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-acerto.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(3000) # Tempo para ouvir a comemoração
            pontos_robocin += 1

        elif chute == 'direita' and defesa == 'esquerda':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-GOL-DIREITA-VOXAR-ESQUERDA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-acerto.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(3000) # Tempo para ouvir a comemoração
            pontos_robocin += 1

    # Se a vez do chute for do Voxar Labs:
    elif vez_chute == 'voxarlabs':
        # Verifica o chute do Voxar Labs e a defesa do RobôCIn:
        if chute == 'centro' and defesa == 'centro':
            cena = pygame.image.load('../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-DEFENDE-CENTRO.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-acerto.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(3000) # Tempo para ouvir a comemoração
            pontos_robocin += 1

        elif chute == 'esquerda' and defesa == 'centro':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-ESQUERDA-ROBOCIN-CENTRO.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-erro.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(900) # Tempo para ouvir as vaias
            pontos_voxar += 1

        elif chute == 'direita' and defesa == 'centro':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-DIREITA-ROBOCIN-CENTRO.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-erro.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(900) # Tempo para ouvir as vaias
            pontos_voxar += 1

        elif chute == 'direita' and defesa == 'direita':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-DEFENDE-DIREITA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-acerto.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(3000) # Tempo para ouvir a comemoração
            pontos_robocin += 1

        elif chute == 'centro' and defesa == 'direita':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-CENTRO-ROBOCIN-DIREITA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-erro.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(900)  # Tempo para ouvir as vaias
            pontos_voxar += 1

        elif chute == 'esquerda' and defesa == 'direita':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-ESQUERDA-ROBOCIN-DIREITA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-erro.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(900) # Tempo para ouvir as vaias
            pontos_voxar += 1

        elif chute == 'esquerda' and defesa == 'esquerda':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-ROBOCIN-DEFENDE-ESQUERDA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-acerto.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(3000) # Tempo para ouvir a comemoração
            pontos_robocin += 1

        elif chute == 'centro' and defesa == 'esquerda':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-CENTRO-ROBOCIN-ESQUERDA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-erro.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(900) # Tempo para ouvir as vaias
            pontos_voxar += 1

        elif chute == 'direita' and defesa == 'esquerda':
            cena = pygame.image.load(
                '../puzzle1/imagens-puzzle1/cenas-partida/puzzle1-cena-VOXAR-GOL-DIREITA-ROBOCIN-ESQUERDA.png')
            exibir_cena(cena)
            pygame.mixer.music.load('../puzzle1/sons-puzzle1/puzzle1-som-erro.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(900) # Tempo para ouvir as vaias
            pontos_voxar += 1

    # Se ainda não houver tido 10 jogadas (5 chutes de cada):
    if (pontos_robocin + pontos_voxar) < 5:
        # Variável para definir se a tela de resultado está ativa (se True). Se False, é devido ao jogador ter fechado a tela:
        status_resultado = True

        # Executa um loop infinito para rodar o puzzle1:
        while status_resultado:

            # Executa um loop percorrendo as ações realizadas no puzzle1:
            for event in pygame.event.get():
                # Se a ação realizada for clicar no botão de fechar a tela, sai do puzzle1:
                if event.type == pygame.QUIT:
                    status_resultado = False
                # Se ação realizada for clicar em uma tecla:
                elif event.type == pygame.KEYDOWN:
                    # Se a tecla for o ENTER, altera a vez do chute e chama a função de alterar a cena do puzzle1, sempre de acordo com a vez do chute:
                    if event.key == pygame.K_SPACE:
                        if vez_chute == 'robocin':
                            vez_chute = 'voxarlabs'
                            partida_defesa()

                        elif vez_chute == 'voxarlabs':
                            vez_chute = 'robocin'
                            partida_chute()

                        status_resultado = False

    # Quando houver tido 5 jogadas na disputa:
    else:
        # Variável para definir se a tela de resultado final está ativa (se True). Se False, é devido ao jogador ter fechado a tela:
        status_resultado_final = True

        #Variável auxiliar para, depois de mostrar o resultado final, ir para uma cena pós-disputa:
        status_continuar_jogo = False

        # Executa um loop infinito para rodar o puzzle1:
        while status_resultado_final:

            # Executa um loop percorrendo as ações realizadas no puzzle1:
            for event in pygame.event.get():
                # Se a ação realizada for clicar no botão de fechar a tela, sai do puzzle1:
                if event.type == pygame.QUIT:
                    status_resultado_final = False
                # Se ação realizada for clicar em uma tecla:
                elif event.type == pygame.KEYDOWN:
                    # Se a tecla for o ENTER, altera a vez do chute e chama a função de exibir o resultado final, sempre de acordo com o placar:
                    if event.key == pygame.K_SPACE:
                        # Se o RobôCIn venceu:
                        if pontos_robocin > pontos_voxar:
                            exibir_resultado_final('robocin')

                        # Se o Voxar Labs venceu:
                        elif pontos_voxar > pontos_robocin:
                            exibir_resultado_final('voxarlabs')

                        status_continuar_jogo = True
                        status_resultado_final = False

        # Leva para a cena pós-disputa de penâltis:
        while status_continuar_jogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    status_continuar_jogo = False

                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            #Se o RobôCIn vencer, avança de cena (para pegar o coletável):
                            if pontos_robocin > pontos_voxar:
                                comecar_coleta()

                            #Se o Voxar Labs vencer, reinicia a disputa (tenta novamente):
                            elif pontos_voxar > pontos_robocin:
                                pontos_robocin, pontos_voxar = 0, 0
                                comecar_partida()

                            status_continuar_jogo = False