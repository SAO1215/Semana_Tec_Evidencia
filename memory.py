"""Memory, puzzle game of number pairs.


"""
#Se declararon todas las variables indefinidas
from random import shuffle
from turtle import up, goto, down, color, begin_fill, forward,\
    left, end_fill, clear, shape, stamp, write, update,\
    ontimer, setup, addshape, hideturtle, tracer,\
    onscreenclick, done

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
terminado = False
# Inicializamos nuestros contador de tapos en 0
counter = 0


def square(x, y):
    """Dibuja un cuadrado blanco con contorno negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convertir (x, y) coordenadas a índice de mosaicos."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierta el recuento de mosaicos en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualice la marca y los mosaicos ocultos según el toque."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        #Se imprimira tap cada que hagamos click en un cuadro del juego
        print("tap")
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        print("tap")


def draw():
    """Dibujar imagen y mosaicos."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 50)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
# El dibujo ha sido completado
terminado = True
print(terminado)
print(counter)
