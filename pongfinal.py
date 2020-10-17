from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from PPlay.mouse import *

#principal
janela = Window(1024,700)
janela.set_title("Pong")

#sprites e gameimages
fundo = GameImage("images\Fbackground.png")
ball = Sprite("images\Fball.png")
pad1 = Sprite("images\pad1.png")
pad2 = Sprite("images\pad2.png")

#velocidade da bola
velx = 300
vely = 300

#ativacao do teclado e do mouse
teclado = Window.get_keyboard()
mouse = Mouse()

#setando as posicoes iniciais da bola, dos pads e suas velocidades de movimentacao
ball.x = janela.width/2 - ball.width/2
ball.y = janela.height/2 - ball.height/2
pad1.x = janela.width/50
pad1.y = janela.height/2
pad2.x = janela.width - pad1.x - pad2.width
pad2.y = janela.height/2
velpad1 = 300
velpad2 = 250

GameScore1 = 0
GameScore2 = 0

GameState = 1

while GameState == 1:

#movimentacao da bola
    ball.x = ball.x + velx*janela.delta_time()
    ball.y = ball.y + vely*janela.delta_time()

#movimentacao do pad1
    if (pad1.y <= 0 and teclado.key_pressed("UP")):
        pad1.y = pad1.y
    elif (pad1.y >= janela.height - pad1.height and teclado.key_pressed("DOWN")):         #impedindo que o pad saia da tela
        pad1.y = pad1.y
    else:
        if (teclado.key_pressed("UP")):
            pad1.y = pad1.y - velpad1*janela.delta_time()
        if (teclado.key_pressed("DOWN")):
            pad1.y = pad1.y + velpad1*janela.delta_time()

#movimentacao do pad2
    if (pad2.y <= 0 and ball.y <= pad2.y):
        pad2.y = pad2.y
    elif (pad2.y >= janela.height - pad2.height and ball.y >= pad2.y):
        pad2.y = pad2.y
    else:
        if (ball.x >= janela.width/2 + 100):
            if (pad2.y < ball.y):
                pad2.y = pad2.y + velpad2*janela.delta_time()
            elif (pad2.y > ball.y):
                pad2.y = pad2.y - velpad2*janela.delta_time()
            else:
                pad2.y = pad2.y

#tratando as colisoes
    if (velx < 0 and Collision.collided(ball, pad1)):
        velx = velx*(-1)
    if (velx > 0 and Collision.collided(ball, pad2)):
        velx = velx*(-1)
    if ((vely > 0 and ball.y >= janela.height - ball.height) or (vely < 0 and ball.y <= 0)):
        vely = vely*(-1)

#resetando a posicao da bola quando um ponto é marcado
    if (ball.x > janela.width):
        ball.x = janela.width/2 - ball.width/2
        ball.y = janela.height/2 - ball.height/2
        GameScore1 += 1
    if (ball.x < 0):
        ball.x = janela.width/2 - ball.width/2
        ball.y = janela.height/2 - ball.height/2
        GameScore2 += 1

    if (GameScore1 == 5 or GameScore2 ==5):
        GameScore1,GameScore2 = 0,0

    fundo.draw()
    janela.draw_text("%d" %GameScore1, 300, 100, 30,(255,255,255),"Arial", False, False)
    janela.draw_text("%d" %GameScore2, janela.width - 300, 100, 30,(255,255,255), "Arial", False, False)
    ball.draw()
    pad1.draw()
    pad2.draw()
    janela.update()

#fps = 1/window.delta_time()
#ballx = ballx + velx*janela.delta_time()
#janela.delta_time() = tempo que demora pra 1 frame
#mouse.is_button_pressed()
#mouse.get_position()

#jogar
#ificuldade
#rank
#sair