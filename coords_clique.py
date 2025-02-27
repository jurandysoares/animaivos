import turtle

# Função chamada quando o mouse é clicado
def exibir_coordenadas(x, y):
    # Exibe as coordenadas no console
    print(f"Coordenadas do clique: x={x:0.0f}, y={y:0.0f}")
    
    # Exibe as coordenadas na tela com o turtle
    turtle.penup()
    turtle.shape('circle')
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(f"({x:0.0f}, {y:0.0f})", font=("Arial", 12, "normal"))
    turtle.stamp()

# Configurações da tela
tela = turtle.Screen()
turtle.setup(1110, 694)
turtle.bgpic("pacote/fundos/fundo-com-degraus.png")
tela.title("Clique para ver as coordenadas do mouse")

# Quando o clique ocorrer, a função exibir_coordenadas é chamada
tela.onclick(exibir_coordenadas)

# Configura o turtle
turtle.speed(0)
turtle.hideturtle()

# Inicia o loop principal
turtle.mainloop()
