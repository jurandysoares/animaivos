from glob import glob
import os
import time
import turtle
from pathlib import Path

# Configurações do balão
global balao
balao = turtle.Turtle()
balao.hideturtle()
balao.down()

def carrega_personagens():
    """Carrega os personagens da animação.

    Carrega os personagens da animação, que são arquivos .gif
    presentes no diretório 'personagens' do pacote.
    """

    cam_personagens = Path(__file__).parent / "personagens"
    cam_atual = Path.cwd()

    os.chdir(cam_personagens.as_posix())
    for img in glob("*.gif"):
        turtle.register_shape(img)

    os.chdir(cam_atual.as_posix())

def fala(personagem: turtle.Turtle, 
         texto: str, 
         angulo: int = 45, 
         distancia: int = 150,
         tempo: float = 5):
    """Exibe um balão de fala para um personagem.

    Exibe um balão de fala para um personagem, com o texto
    passado como parâmetro, em um ângulo e distância específicos.
    """
    
    x,y = personagem.pos()
    balao.goto(x, y)   
    balao.left(angulo)
    balao.forward(distancia)
    balao.write(fala)
    time.sleep(tempo)
    balao.undo()
    balao.undo()
    balao.undo()

def carrega_img_fundo(img_fundo: str):
    """Carrega uma imagem de fundo para a tela.

    Carrega uma imagem de fundo para a tela, que é um arquivo .gif
    presente no diretório 'fundos' do pacote.
    """

    cam_img_fundo = Path(__file__).parent / "fundos" / img_fundo

    if cam_img_fundo.exists() and cam_img_fundo.is_file():
        turtle.bgpic(cam_img_fundo.as_posix())
    else:
        print(cam_img_fundo.as_posix())
        print('Imagem de fundo não encontrada!')

