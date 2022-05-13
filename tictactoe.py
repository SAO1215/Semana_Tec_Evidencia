"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import up, goto, down, circle, update, done, color, width
from turtle import setup, hideturtle, tracer, onscreenclick
from freegames import line

board = ["", "", "", "", "", "", "", "", ""]


def grid():
    """Dibujar tablero de tic-tac-toe"""
    color("black")
    width(3)
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibujar jugador X"""
    color("red")
    width(5)
    line(x + 20, y + 20, x + 120, y + 120)
    line(x + 20, y + 120, x + 120, y + 20)


def drawo(x, y):
    """Dibujar jugador O"""
    color("blue")
    width(5)
    up()
    goto(x + 67, y + 12)
    down()
    circle(55)


def floor(value):
    """Redondear valor hasta la cuadricula con tamaño 133"""
    return ((value + 200) // 133) * 133 - 200


"""Variables de estado y jugador a dibujar"""
state = {'player': "x"}


def tap(x, y):
    """Dibujar X o O en el cuadro"""
    x = floor(x)
    y = floor(y)

    """Condicion si se llena todo el tablero"""
    if all(board):
        print("Ya no hay espacio")
        return

    """Determinar x y y del area del tablero"""
    x_area = (x + 200) // 133
    y_area = (200 - y) // 133

    """Determinar las areas y imprimir la que se selecciono"""
    area = int(x_area + y_area * 3) - 3
    print("Seleccionaste el espacio", area, end="")

    """Determinar si una casilla ya esta ocupada"""
    if board[area]:
        print("-- ya se encuentra ocupada")
        return
    else:
        print()

    """Llenar arreglo con X o O"""
    board[area] = state['player']

    """Si el turno es de X, cambiar a O"""
    if state['player'] == "x":
        state['player'] = "o"
    else:
        state['player'] = "x"

    """Dibujar X o O dependiendo del turno"""
    if state['player'] == "x":
        drawx(x, y)
        update()
    else:
        drawo(x, y)
        update()


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
