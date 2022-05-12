"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import up, goto, down, circle, update, done, color
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
    color("red")
    line(x + 20, y + 20, x + 120, y + 120)
    line(x + 20, y + 120, x + 120, y + 20)

def drawo(x, y):
    """Dibujar jugador O"""
    color("blue")
    up()
    goto(x + 67, y + 12)
    down()
    circle(55)


def floor(value):
    """Redondear valor hasta la cuadricula con tamañño 133"""
    return ((value + 200) // 133) * 133 - 200


"""Variables de estado y jugador a dibujar"""
state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Dibujar X o O en el cuadro"""
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
