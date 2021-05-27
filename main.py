from os import system
from time import sleep

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
    print(f'\n\n[{l_vermelho}i{no_color}] {l_vermelho}Instalando recursos...\n\n')
    system('pkg install mpg123')
    
def gtts():
    system('clear')
    
    tts = gTTS(text=texto, lang=idioma, slow=False)
    tts.save("gtts.mp3")
    system("mpg123 gtts.mp3")
