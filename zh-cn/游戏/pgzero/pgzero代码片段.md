```python
import pgzrun

y = 100

def draw():
   screen.fill('white')
   screen.draw.filled_circle((400,y),30,'red')

def update():
   global y
   y = y + 1

pgzrun.go()
```

结构

```
.
├── images/
│   └── alien.png
└── intro.py
```

一段完整的游戏代码

```python
import pgzrun

WIDTH = 1300
HEIGHT = 600
NUM = 3
balls = []
for i in range(NUM):
    ball = Actor("ball")
    ball.x = 50 * i + 100
    ball.y = 100
    ball.dx = 5 + i
    ball.dy = 5 + i
    balls.append(ball)

def draw():
    screen.fill((255,255,255))
    for ball in balls:
        ball.draw() 
    
def update():
    for ball in balls:
        ball.x += ball.dx
        ball.y += ball.dy
        if ball.right > WIDTH or ball.left < 0:
            ball.dx = - ball.dx
        if ball.bottom > HEIGHT or ball.top < 0:
            ball.dy = -ball.dy 
        
pgzrun.go()
```

