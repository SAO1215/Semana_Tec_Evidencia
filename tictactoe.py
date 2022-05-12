"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import up, goto, down, circle, update, done
from turtle import setup, hideturtle, tracer, onscreenclick
from freegames import line

def grid():
    """Dibujar tablero de tic-tac-toe"""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    """Dibujar jugador X"""
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

def drawo(x, y):
    """Dibujar jugador O"""
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Redondear valor hasta la cuadricula con tamañño 133"""
    return ((value + 200) // 133) * 133 - 200


"""Variables de estado y jugador a dibujar"""
state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Dibujar X o O en el cuadro seleccionado"""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
