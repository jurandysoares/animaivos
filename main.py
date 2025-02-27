"""
Módulo principal
"""

import turtle

from pacote.nucleo import carrega_img_fundo, carrega_personagens, fala

# Do módulo menus, do pacote ______, import o menu_principal
from pacote.menus import menu_principal

def cena_demo():
    """Cena de demonstração."""
    turtle.setup(1110, 694)
    carrega_img_fundo("fundo-com-degraus.png")
    
# Renomei a função seguindo o padrao <cena_descricao_breve_cena>
def cena1():
    """
    Descrição da cena 1
    """
    pass

# Renomei a função seguindo o padrao <cena_descricao_breve_cena>
def cena2():
    """
    Descrição da cena 2
    """    
    pass

# Renomei a função seguindo o padrao <cena_descricao_breve_cena>
def cena3():
    """
    Descrição da cena 3
    """    
    pass

# Renomei a função seguindo o padrao <cena_descricao_breve_cena>
def cena4():
    """
    Descrição da cena 4
    """    
    pass


# Função principal
def main():
    carrega_personagens()    
    print("Os seguintes personagens foram carregados:")
    formas_gif = [forma for forma in turtle.getshapes() if forma.endswith('.gif')]
    print('\n'.join(formas_gif))

    op = int(input(menu_principal))
    while op != 5:
        if op == 1:
            cena1()
        elif op == 2:
            cena2()
        elif op == 3:
            cena3()
        elif op == 4:
            cena4()
        else:
            print("Opção inválida.")
            
        op = int(input(menu_principal))

    # turtle.done()

# Chamada da função principal
if __name__ == "__main__":
    main()

