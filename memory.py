"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""
#Se declararon todas la variables indefinidas mostradas por flake8
from random import shuffle
from turtle import up, goto, down, color, begin_fill, forward,\
    left, end_fill, clear, shape, stamp, write, update,\
    ontimer, setup, addshape, hideturtle, tracer,\
    onscreenclick, done

from freegames import path

#Se espeficio de cuanto cuadros iba ser nuestro memory y se agrego un contador para el contador de taps 
car = path('car.gif')
tiles = list(range(8)) * 2
state = {'mark': None}
hide = [True] * 16
terminado = False
# Contador de taps
global counter 
counter = 0

#Se declararon los colores del recuadro y espeficiamos con el ciclo for el numero de cuadros por lado
def square(x, y):
    """Dibuja un cuadrado blanco con contorno negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(100)
        left(90)
    end_fill()


def index(x, y):
    """Convertimos (x, y)coordenadas a índice de mosaicos."""
    return int((x + 200) // 100 + ((y + 200) // 100) * 4)


def xy(count):
    """Conviertimos el recuento de mosaicos a coordenadas (x, y)."""
    return (count % 4) * 100 - 200, (count // 4) * 100 - 200


def tap(x, y):
    global counter
    """Actualice la marca y los mosaicos ocultos según el toque."""
    spot = index(x, y)
    mark = state['mark']
    
    #Especificamos que ya sea si le atinas a nos mosaicos y no se imprima tap cada vez que le piques a un cuadro
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        print("tap")
        counter=counter+1
        
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        print("tap")
        counter=counter+1
   


def draw():
    """Se dibujo la imagen y los mosaicos."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 50, 'normal'))

    update()
    ontimer(draw, 70)

#Mandamos llamar todas nuestras funciones con nuetro mensaje final y nuestro contador de taps.
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
print("¡TERMINASTE EL JUEGO!")
print("Numero de taps: ",counter)
print(terminado)