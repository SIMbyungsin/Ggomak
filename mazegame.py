from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

__ = False


class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            speed = 20,
            model = 'sphere',
            collider = 'mesh',
            scale = 1,
            texture = 'marble_bust_01_4k.blend/textures/marble_bust_01_diff_4k.jpg'
        )

class Warp(Entity):
    def __init__(self, i, j):
        super().__init__(
            warp = Entity(
                model = 'cube',
                scale = (5, 17, 5),
                color = color.gray,
                position = (i * 5, -3, j * 5),
                collider = 'box',
                texture = 'marble_bust_01_4k.blend/textures/marble_bust_01_diff_4k.jpg'
            )
        )
        self.a = player

        def update(self):
            print(player.position)
            self.abcd()

        def abcd(self): #플레이어와 충돌을 감지하는 함수
            if self.warp.intersects(self.a):
                self.a.position = (95, 30, 90)
        
        def clear(self):
            dis = (self.player.position - self.position).length()
            print(dis)
            if dis < 3:
                self.player.position = (95, 3, 90)

class Exit(Entity):
    def __init__(self, i, j):
        super().__init__(
            model = 'cube',
            scale = (5, 5, 5),
            color = color.gray,
            position = (i * 5, -3, j * 5),
            collider = 'box'
        )
        self.player = player
        self.text = Text(
            text = 'hitomi.la/278336',
            scale = 2,
            origin = (0, 0),
            visible = False
        )
    def update(self):
        self.clear()

    def clear(self):
            dis = (self.player.position - self.position).length()
            print(dis)
            if dis < 3:
             self.player.enabled = False
             self.text.visible = True

def input(key):
    if key == 'escape':
        application.quit()

player = Player()

ground = Entity(
    model = 'plane',
    color = color.gray,
    position = (0, -5, 0),
    scale = (3000, 1, 3000),
    collider = 'mesh',
    texture = 'metal_plate_4k.blend/textures/metal_plate_disp_4k.png'
)

MAP = [
    [11, __ ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33],
    [11, 'p' ,13 ,14, __, __, __, 18, __, __, __, 22, 23, 24, __, __, __, __, 29, __, 31, 32, 33],
    [11, __ ,13 ,14, 15, 16, __, 18, __, 20, __, 22, __, __, __, 26, 27, __, 29, __, 31, 32, 33],
    [11, __ ,__ ,__, 15, 16, __, __, __, 20, __, 22, __, 24, __, 26, __, __, 29, __, __, __, 33],
    [11, 'w' ,__ ,14, 15, __, 17, __, 19, 20, __, __, __, 24, 25, 26, 27, __, 29, 30, __, 32, 33],
    [11, 12 ,__ ,__, __, __, __, __, 19, 20, __, 22, 23, 24, __, __, 27, __, 29, 30, 'Bust', 32, 33],
    [11, 12 ,'Bust' ,14, 15, 16, 17, 18, 19, 20, 21, __, __, __, __, __, 27, __, 29, 30, 31, 32, 33],
    [11, 12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, __, 23, 24, 25, __, __, __, 29, 30, 31, 32, 33],
    [11, 12 ,__ ,__, __, 16, __, __, __, __, 21, __, 23, 24, 25, __, 27, __, __, 30, 31, 32, 33],
    [11, 12 ,__ ,14, __, __, __, 18, __, 20, 21, __, 23, 'Bust', 25, __, 27, __, __, __, __, 32, 33],
    [11, 12 ,__ ,14, __, 16, __, 18, __, __, __, __, 23, __, 25, __, __, __, 29, 30, __, 32, 33],
    [11, 12 ,__ ,14, __, 16, __, 18, 19, 20, __, 22, 23, __, __, __, 27, __, 29, 30, __, 32, 33],
    [11, 12 ,__ ,__, __, __, __, 18, 19, 20, __, 22, 23, 24, 25, __, __, __, 29, __, __, 32, 33],
    [11, 12 ,__ ,14, __, 16, __, 18, __, __, __, __, __, __, 25, 26, __, 28, 29, __, 31, 32, 33],
    [11, 12 ,__ ,14, __, 16, __, 18, __, 20, 21, 22, 23, __, 25, __, __, 28, 29, __, 31, 32, 33],
    [11, __ ,__ ,14, 15, 16, __, 18, __, 20, 21, __, 23, __, 25, 26, __, 28, 29, __, __, __, 33],
    [11, 12 ,__ ,__, __, __, __, 18, __, __, __, __, 23, __, 25, 26, __, __, __, __, 31, __, 33],
    [11, 12 ,13 ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 'Bust', 25, 26, 27, 28, 29, __, 31, __, 33],
    [11, __ ,__ ,__, __, __, __, __, __, __, __, __, __, __, __, __, __, __, __, __, 31, 'Bust', 33],
    [11, 12 ,'e' ,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33],

]

Bust = Entity(
    model = 'marble_bust_01_4k.fbx',
    texture = 'textures/marble_bust_01_diff_4k.jpg',
    scale = 0.5,
    color = color.gray,
    rotation = (0.100,0),
    position = ('Bust')
    
  
)

for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        if MAP[i][j] :
            if MAP[i][j] == 'p':
                print("abc")
                player.position = (i * 5, 50, j * 5)
                continue
            if MAP[i][j] == 'e':
                exit == Exit(i,j)
                continue
            if MAP[i][j] == 'w':
                warp = Warp(i, j)
                continue
            
            
            wall = Entity(
                model = 'cube',
                color = color.gray,
                scale = (5, 15, 5),
                position = (i * 5, -2, j * 5),
                collider = 'box',
                texture = 'marble_bust_01_4k.blend/textures/marble_bust_01_diff_4k.jpg'
                )


app.run()