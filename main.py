from os import system
from time import sleep
from gtts import gTTS

# Cores

f_vermelho = '\033[1;41m'
f_verde = '\033[1;42m'
f_amarelo = '\033[1;43m'

l_amarelo = '\033[1;33m'
l_vermelho = '\033[1;31m'
l_verde = '\033[1;32m'

no_color = '\033[m'

# GTTS

def gtts():
    system('clear')
    print(f'{f_vermelho}GTTS by @ONELOST.EXE{no_color}\n')
    texto = input(f'{no_color}Digite o texto:{l_amarelo} ')
    idioma = input(f'{no_color}Digite o idioma:{l_amarelo} ')
    tts = gTTS(text=texto, lang=idioma, slow=False)
    tts.save("gtts.mp3")
    print(f'\n{f_vermelho}Resultado:{no_color}\n')
    system("mpg123 gtts.mp3")

gtts()
