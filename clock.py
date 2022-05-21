from graphics import *
import math
window = GraphWin("Draw A Clock",
                   640,
                   480,
                   autoflush=False)
# Define the clock center
cx = 200
cy = 150# Define length of minute bars around the clock
len = 100# Current arrow angle
angle = 0
inner_circle = Circle(Point(cx, cy), 120)
inner_circle.setFill('red')
outer_circle = Circle(Point(cx, cy), 130)
outer_circle.setFill('black')
outer_circle.draw(window)
inner_circle.draw(window)
for i in range(0, 16 * 4):  # calculate end points of 1 minute bars
  # with the help of trigonometry
  ox = cx + math.sin(angle) * len*1.1
  oy = cy + math.cos(angle) * len*1.1
  ex = cx + math.sin(angle) * len
  ey = cy + math.cos(angle) * len
  
  pt = Point(ox, oy)
  line = Line(Point(ex, ey), pt)
  line.setWidth(2)
  line.setFill('gray85')
  line.draw(window)  # move the angle by a fraction of a circle
  angle += 0.2618 / 15 * 6
# reset the angle to start over
angle = 0
for i in range(0, 12):  # calculate end points of 5 minute bars
  # with the help of trigonometry
  ox = cx + math.sin(angle) * len*1.2
  oy = cy + math.cos(angle) * len*1.2
  ex = cx + math.sin(angle) * len
  ey = cy + math.cos(angle) * len
  pt = Point(ox, oy)
  line = Line(Point(ex, ey), pt)
  line.setWidth(10)
  line.setFill('black')
  line.draw(window)  # move the angle by a fraction of a circle
  angle += 0.2618 / 3 * 6
def draw_bars(number,
              angle,
              interval,
              length,
              width,
              color,
              distance,
              tip=0):
 
  for i in range(0, 16 * 4):
    # calculate end points of 1 minute bars
    # with the help of trigonometry
    ox = cx + math.sin(angle) * length * distance
    oy = cy + math.cos(angle) * length * distance
    ex = cx + math.sin(angle) * length
    ey = cy + math.cos(angle) * length
    pt = Point(ox, oy)
    line = Line(Point(ex, ey), pt)
    line.setWidth(width)
    line.setFill(color)
    line.draw(window)    # move the angle by a fraction of a circle
    angle += interval
    return line
draw_bars(1, 15, 0, 1, 10, 'cyan', 70)
draw_bars(1, 47, 0, 1, 5, 'magenta', 100)
pythonic = Text(Point(cx, cy + 40), "Dayal Original")
pythonic.draw(window)
middle = Circle(Point(cx, cy), 10)
middle.setFill('cyan')
middle.draw(window)
p1 = Point(10, 10)
p2 = Point(130, 50)
lin = Line(p1,p2)
lin.setWidth(3)
lin.setFill('blue')
lin.p1 = Point(400,230)
lin.draw(window)
length = 100
distance = 1
angle = 10# arrow’s center point
cx = 200
cy = 150
for i in range(10000):  # <drawing commands for ith frame>
  lin.undraw()
  ox = cx + math.sin(angle) * length * distance
  oy = cy + math.cos(angle) * length * distance
  ex = cx + math.sin(angle) * length
  ey = cy + math.cos(angle) * length
  lin.p1 = Point(cx, cy)
  lin.p2 = Point(ex, ey)
  lin.draw(window)
  angle -= 0.01
  update(24)



