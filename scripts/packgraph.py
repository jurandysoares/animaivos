import os
import inspect
import importlib
from graphviz import Digraph
import os
import sys

# Nome do pacote que deseja mapear
PACOTE = "pacote"

def listar_modulos(pacote):
    """Encontra todos os módulos dentro de um pacote."""
    modulos = []
    pacote_caminho = os.path.dirname(importlib.import_module(pacote).__file__)
    
    for root, _, files in os.walk(pacote_caminho):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                modulo_relativo = os.path.relpath(os.path.join(root, file), pacote_caminho)
                modulo_nome = f"{pacote}." + modulo_relativo.replace(os.sep, ".").replace(".py", "")
                modulos.append(modulo_nome)
    
    return modulos

def obter_funcoes(modulo):
    """Obtém todas as funções públicas de um módulo."""
    try:
        mod = importlib.import_module(modulo)
        return [nome for nome, obj in inspect.getmembers(mod, inspect.isfunction)]
    except Exception:
        return []

def gerar_diagrama(pacote):
    """Gera um diagrama mental usando Graphviz."""
    sys.path.append(os.getcwd())
    dot = Digraph(comment=f'Mapa Mental do Pacote {pacote}')
    dot.attr(rankdir="LR", size="10")

    modulos = listar_modulos(pacote)

    for modulo in modulos:
        dot.node(modulo, modulo, shape="box", style="filled", fillcolor="lightblue")

        funcoes = obter_funcoes(modulo)
        for func in funcoes:
            dot.node(f"{modulo}.{func}", func, shape="ellipse", style="filled", fillcolor="lightyellow")
            dot.edge(modulo, f"{modulo}.{func}")

    dot.render("mapa_mental", format="png", cleanup=True)
    print("Mapa mental gerado: mapa_mental.png")

# Gerar o diagrama
gerar_diagrama(PACOTE)
