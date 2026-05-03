from pygame import mixer
from emoji import emojize
from time import sleep
from PIL import Image

# Boa prática: Iniciar o mixer logo no começo do programa
mixer.init()

for c in range(10, 0, -1):
    # Correção: Uso de ponto e vírgula ';'. 4 = sublinhado, 33 = texto amarelo
    print(f'\033[4;33m{c}\033[m')
    sleep(1)

    if c == 1:
        # Correção da cor: 1 = negrito, 36 = ciano
        print(emojize('Parabéns! Este é o \033[1;36mFIM\033[m 🎆'))
        sleep(0.5)
        img = Image.open('familia-comemorando.png')
        img.show()

        # --- PRIMEIRO ÁUDIO ---
        mixer.music.load('fogo-de-artificio.mp3')
        mixer.music.play()

        # O SEGREDO: Fazer o programa esperar a música 1 terminar
        while mixer.music.get_busy():
            sleep(0.1)  # Uma pausa mínima para não sobrecarregar o computador

        # --- SEGUNDO ÁUDIO ---
        # Só vai carregar e tocar quando o áudio de cima terminar totalmente
        mixer.music.load('ElevenLabs_Série_explosiva_de_fogos_de_artifício_durante_a_celebração_do_Ano_Novo_Chinês__estrondos_altos_e_est.mp3')
        mixer.music.play()

        # Fazer o programa esperar a música 2 terminar antes de fechar a janela
        while mixer.music.get_busy():
            sleep(0.1)