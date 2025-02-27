# Animaivos

Bem-vindo ao repositório do projeto Animaivos!

## Animação final

Faça uma animação que atenda aos seguintes requisitos:

1. Ter 4 cenas com fundos distintos e que tenham obstáculos
2. Ter 2 ou mais personagens por cenas
3. Cada cena deverá ser implementada em uma função com nome mnemônico
4. A animação deverá ser feita no módulo `turtle` do Python
5. Pelo menos uma das cenas deve contemplar:

   1. Repetição 3 ou mais vezes com laço `while`
   2. Condição com `if`/`elif`/`else`
   3. Seguir instruções de um arquivo
   4. Ter diálogo com 10 falas

## Configuração do usuário para o Git

1. Abra um terminal (No Windows, o Git Bash)
2. Liste as configurações globais do Git.
   
   Execute: `git config --global --list`
   
3. Configure o nome do usuário, se necessário.
   
   Execute: `git config --global user.name "Nome Sobrenome"`

4. Configure o endereço de e-mail do usuário, se necessário.
  
   Execute: `git config --global user.email "usuario@dominio"`

5. Listar as configurações novamente conforme passo 3.

## Execução interativa

```
$ python -i main.py 
Os seguintes personagens foram carregados:
_cat.gif
_elephant.gif
_mouse.gif
cat_.gif
elephant_.gif
mouse_.gif

    Animação de Fulano, Beltrano e Sicrano
    ======================================

    Listagem de cenas:

       1. Cena 1
       2. Cena 2
       3. Cena 3
       4. Cena 4
       5. Sair

    Escolha sua opção: 5
>>> cena_demo()
>>> fala(gato, "Oi!", distancia=50, angulo=135, tempo=1)
>>> habilita_clique()
>>> turtle.exitonclick()
>>> exit()
```
