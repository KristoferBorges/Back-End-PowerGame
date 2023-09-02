from random import randint
from pygame import mixer

# Caminho do arquivo de dados
path = "app/data/storage.xlsx"

# Musicas
mixer.init()
selecionar = mixer.Sound(r'app\media\music\escolha12.wav')
lose = mixer.Sound(r'app\media\music\lose.wav')
win = mixer.Sound(r'app\media\music\winwin.wav')
boss = mixer.Sound(r'app\media\music\infernal2.wav')
bonus = mixer.Sound(r'app\media\music\bonus.wav')
critico = mixer.Sound(r'app\media\music\critico.wav')
roar1 = mixer.Sound(r'app\media\music\Roar1.mp3')
roar2 = mixer.Sound(r'app\media\music\Roar2.mp3')
roar3 = mixer.Sound(r'app\media\music\Roar3.mp3')
roar4 = mixer.Sound(r'app\media\music\Roar4.mp3')
roarlose = mixer.Sound(r'app\media\music\RoarLose.mp3')
roardead = mixer.Sound(r'app\media\music\Roardead.mp3')

# Cores
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
ciano = '\033[36m'
normal = '\033[m'

# Variáveis importantes!
resultado = ''
escolha = ''
skipBoss = 0
choiceBonus = 0
escolha_usar_item = 0
soma_nivel = 0
aposta = 0
multiplicador = 0.00
lv_monster_print = 0
lv_choice = 0
roarChoice = 0

# pontos
point = 0
pointx = randint(1, 10)