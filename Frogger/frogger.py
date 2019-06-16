import arcade
import random

WIDTH = 700
HEIGHT = 700
'''
    colors = [
    [1, arcade.color.WHITE],
    [2, arcade.color.GREEN],
    [4, arcade.color.DARK_BLUE],
    [8, arcade.color.BLUE],
    [16, arcade.color.BROWN],
    [32, arcade.color.PURPLE],
    [64, arcade.color.BLACK],
    [128, arcade.color.RED],
    [256, arcade.color.LIGHT_GREEN]]
'''
global frog_x, frog_y
frog_lives = 3

frog_x = 0
frog_y = 0
game_counter = 0
counter = 0

columns = 24
rows = 16

x = 0
y = 0

screen = [[0 for x in range(columns)] for y in range(rows)]
logs = [0 for x in range(5)]
cars = [0 for x in range(5)]
cars_type = [0 for x in range(5)]

square_size = 29

for x in range(columns):
    screen[0][x] = 64

for x in range(columns):
    screen[1][x] = 32

for x in range(columns):
    screen[2][x] = 64

for x in range(columns):
    screen[3][x] = 64

for x in range(columns):
    screen[4][x] = 64

for x in range(columns):
    screen[5][x] = 64

for x in range(columns):
    screen[6][x] = 64

for x in range(columns):
    screen[7][x] = 32
for x in range(columns):
    screen[8][x] = 8

for x in range(columns):
    screen[9][x] = 8

for x in range(columns):
    screen[10][x] = 8

for x in range(columns):
    screen[11][x] = 8

for x in range(columns):
    screen[12][x] = 8

for x in range(columns):
    if x % 4 == 0 or x % 4 == 1:
        screen[13][x] = 8
    else:
        screen[13][x] = 256

for x in range(columns):
    if x % 4 == 0 or x % 4 == 1:
        screen[14][x] = 8
    else:
        screen[14][x] = 256

for x in range(columns):
    screen[15][x] = 256

screen[0][0] |= 2

texture_frog = arcade.load_texture("frogger.png", 0, 0, 50, 75, False, True)
texture_log = arcade.load_texture("frogger.png", 376, 250, 200, 75, False, False)
texture_car_blue = arcade.load_texture("frogger.png", 7, 485, 150, 67, False, False)
texture_car_green = arcade.load_texture("frogger.png", 150, 485, 150, 67, False, False)
texture_car_yellow = arcade.load_texture("frogger.png", 300, 485, 150, 67, False, False)



def random_logs(index,color_on, color_off):
    global logs
    if(logs[index] < 0 ):
        logs[index] = random.randint(0,7)
        if(logs[index] == 0):
            logs[index] = 3
        else:
            logs[index] = 0

    logs[index] -= 1

    if(logs[index] > 0):
        return color_on
    else:
        return color_off

def random_cars(index,color_on, color_off):
    global cars
    if(cars[index] < 0 ):
        cars[index] = random.randint(0,7)
        if(cars[index] == 0):
            cars[index] = 2
        else:
            cars[index] = 0
        cars_type[index] = index%3

    cars[index] -= 1

    if(cars[index] > 0):
        return color_on
    else:
        return color_off

def on_update(delta_time):
    global screen, frog_x, frog_y, square_size, columns,rows,logs,cars, counter,frog_lives

    counter += 1

    for x in range(columns):
        if(screen[2][columns - 1 - x - 1] & 2 == 2):
            screen[2][columns - 1 - x - 1] &= ~2
        screen[2][columns - 1 - x] = screen[2][columns - 1 - x - 1]
    screen[2][0] = random_cars(0, 128, 64)

    for x in range(columns):
        if(screen[3][columns - 1 - x - 1] & 2 == 2):
            screen[3][columns - 1 - x - 1] &= ~2
        screen[3][columns - 1 - x] = screen[3][columns - 1 - x - 1]
    screen[3][0] = random_cars(1, 128, 64)

    for x in range(1,columns):
        if(screen[4][x] & 2 == 2):
            screen[4][x] &= ~2
        screen[4][x-1] = screen[4][x]
    screen[4][columns-1] = random_cars(2, 128, 64)

    for x in range(columns):
        if (screen[5][columns - 1 - x - 1] & 2 == 2):
            screen[5][columns - 1 - x - 1] &= ~2
        screen[5][columns - 1 - x] = screen[5][columns - 1 - x - 1]
    screen[5][0] = random_cars(3, 128, 64)

    for x in range(columns):
        if(screen[6][columns - 1 - x - 1] & 2 == 2):
            screen[6][columns - 1 - x - 1] &= ~2
        screen[6][columns - 1 - x] = screen[6][columns - 1 - x - 1]
    screen[6][0] = random_cars(4, 128, 64)

    if counter%2 == 0:
        if screen[frog_y][frog_x] & ~2 == 16:
            if(frog_y == 8 or frog_y == 10 or frog_y == 12):
                move_frog(1,0)
            elif(frog_y == 9 or frog_y == 11):
                move_frog(-1, 0)
            else:
                move_frog(0, 0)

        for x in range(columns):
            if(screen[8][columns - 1 - x - 1] & 2 == 2):
                screen[8][columns - 1 - x - 1] &= ~2
            screen[8][columns - 1 - x] = screen[8][columns - 1 - x - 1]
        screen[8][0] = random_logs(0,16,8)

        for x in range(1,columns):
            if(screen[9][x] & 2 == 2):
                screen[9][x] &= ~2
            screen[9][x-1] = screen[9][x]
        screen[9][columns-1] = random_logs(1,16,8)

        for x in range(columns):
            if(screen[10][columns - 1 - x - 1] & 2 == 2):
                screen[10][columns - 1 - x - 1] &= ~2
            screen[10][columns - 1 - x] = screen[10][columns - 1 - x - 1]
        screen[10][0] = random_logs(2,16,8)

        for x in range(1,columns):
            if(screen[11][x] & 2 == 2):
                screen[11][x] &= ~2
            screen[11][x - 1] = screen[11][x]
        screen[11][columns-1] = random_logs(3,16,8)

        for x in range(columns):
            if(screen[12][columns - 1 - x - 1] & 2 == 2):
                screen[12][columns - 1 - x - 1] &= ~2
            screen[12][columns - 1 - x] = screen[12][columns - 1 - x - 1]
        screen[12][0] = random_logs(4,16,8)

    if(screen[frog_y][frog_x] == 128 or screen[frog_y][frog_x] == 8):
        frog_lives -= 1
        frog_x = 0
        frog_y = 0
    move_frog(0, 0)


def on_draw():
    global cars_type,cars,logs, texture_car_blue, texture_car_green,texture_car_green,frog_lives, game_counter
    arcade.start_render()
    texture_level_1 = arcade.load_texture("level1.png", 0,0, square_size*24,square_size*16 , False, False)
    arcade.draw_texture_rectangle(texture_level_1.width/2, texture_level_1.height/2,texture_level_1.width, texture_level_1.height,texture_level_1, 0, 255)
    scale = .5
    scale_car = .4

    if (frog_lives > 0 and frog_y == 15):
        arcade.draw_text("You win, your time is "+str(game_counter/5)+" \nPress space to restart", 100, 18 * square_size,
                         arcade.color.RED, 30)
    elif (frog_lives <= 0):
        arcade.draw_text("Game Over ! Press space to restart" , 100, 18 * square_size,
                         arcade.color.RED, 30)
    else:
        game_counter += 1

        arcade.draw_text("Lives: " + str(frog_lives) + " Time: " + str(game_counter / 5), 100, 18 * square_size,
                         arcade.color.RED, 30)
        for y in range(rows):
            prev_color = 0
            for x in range(columns):
                b_color = arcade.color.WHITE
                if screen[y][x] & 0x02:
                    b_color = arcade.color.GREEN

                if screen[y][x] & 1:
                    l_color = arcade.color.WHITE
                elif screen[y][x] & 4:
                    l_color = arcade.color.DARK_BLUE
                elif screen[y][x] & 8:
                    l_color = arcade.color.BLUE
                elif screen[y][x] & 16:
                    l_color = arcade.color.BROWN
                elif screen[y][x] & 32:
                    l_color = arcade.color.PURPLE
                elif screen[y][x] & 64:
                    l_color = arcade.color.BLACK
                elif screen[y][x] & 128:
                    l_color = arcade.color.RED
                elif screen[y][x] & 256:
                    l_color = arcade.color.LIGHT_GREEN

                if(l_color == arcade.color.RED):
                    if(screen[y][x]&~0x02 != prev_color&~0x02):
                        if(y>=2 and y<=6 and cars_type[y-2] == 0):
                            texture_car = texture_car_green
                        elif (y >= 2 and y <= 6 and cars_type[y-2] == 1):
                            texture_car = texture_car_yellow
                        else:
                            texture_car = texture_car_blue
                        arcade.draw_texture_rectangle(x * square_size, y * square_size+square_size/2 ,scale_car *texture_car.width,scale_car * texture_car.height, texture_car,0,255)
                elif (l_color == arcade.color.BROWN):
                    if(screen[y][x]&~0x02 != prev_color&~0x02):
                        arcade.draw_texture_rectangle(x * square_size+square_size/2, y * square_size+square_size/2 ,scale *texture_log.width,scale * texture_log.height, texture_log,0,255)

                if(b_color == arcade.color.GREEN):
                    arcade.draw_texture_rectangle(x * square_size+square_size/2, y * square_size+square_size/2, scale * texture_frog.width, scale * texture_frog.height, texture_frog, 0,255)

                prev_color = screen[y][x]

def move_frog(x,y):
    global frog_x, frog_y, columns
    screen[frog_y][frog_x] &= ~2

    frog_x += x
    if (frog_x <0):
        frog_x = 0
    if (frog_x >=columns):
        frog_x = columns-1

    frog_y += y
    if (frog_y <0):
        frog_y = 0
    if (frog_y >=rows):
        frog_y = rows-1

    screen[frog_y][frog_x] |= 2

def on_key_press(key, modifiers):

    if key == arcade.key.W:
        move_frog(0,1)

    if key == arcade.key.A:
        move_frog(-1, 0)

    if key == arcade.key.S:
        move_frog(0, -1)

    if key == arcade.key.D:
        move_frog(1, 0)


def on_key_release(key, modifiers):
    global frog_lives,game_counter,frog_y,frog_x

    if key == arcade.key.SPACE and (frog_lives == 0 or (frog_lives > 0 and frog_y == 15)):
        frog_lives = 3
        game_counter = 0
        frog_y = 0
        frog_x = 0

def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1 / 5)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
