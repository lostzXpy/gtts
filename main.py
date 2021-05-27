from os import system
from time import sleep
import subprocess

# Cores

f_vermelho = '\033[1;41m'
f_verde = '\033[1;42m'
f_amarelo = '\033[1;43m'

l_amarelo = '\033[1;33m'
l_vermelho = '\033[1;31m'
l_verde = '\033[1;32m'

no_color = '\033[m'

# Instalação

def install():
    check = subprocess.check_output('pkg install mpg123', shell=True)
    if '0 upgraded, 0 newly installed, 0 to remove and 1 not upgraded' not in check.decode():
        print(f'\n\n[{l_vermelho}i{no_color}] {l_vermelho}Instalando recursos...\n\n')
        system('pkg install mpg123')
    else:
        print(f'\n\n[{l_vermelho}i{no_color}] {l_vermelho}Iniciando...\n\n')
        sleep(1)
# GTTS

def gtts():
    system('clear')
    logo = f'{f_vermelho}GTTS by @ONELOST.EXE{no_color}\n'
    text = input('{f_amarelo}Digite o texto:{no_color} ')
    idioma = input('{f_amarelo}Digite o idioma:{no_color} ')
    tts = gTTS(text=texto, lang=idioma, slow=False)
    tts.save("gtts.mp3")
    print(f'\n{f_vermelho}Resultado:{no_color}\n')
    system("mpg123 gtts.mp3")

install()
gtts()
