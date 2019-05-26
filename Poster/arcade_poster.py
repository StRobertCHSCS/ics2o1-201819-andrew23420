import arcade
import math
import webbrowser

WIDTH = 1024
HEIGHT = 768

alpha = 0
radius = 100
x1 = 0
y1 = 0
x2 = 0
y2 = 0
x3 = 0
y3 = 0

my_button = [825 - 150, 768 - 266 - 150, 825 + 150, 768 - 266 + 150]

def on_update(delta_time):
    global alpha
    alpha = (alpha + .01)
    if alpha > 2*math.pi:
        alpha = 0



def on_draw():
    global alpha,x1,y1,x2,y2,x3,y3
    arcade.start_render()
    # Draw in here...arcade_template

    x1 = 200 + radius*math.cos(alpha)
    y1 = 200 + radius*math.sin(alpha)

    x2 = 200 + radius * math.cos(alpha + 2*math.pi/3)
    y2 = 200 + radius * math.sin(alpha + 2*math.pi/3)

    x3 = 200 + radius * math.cos(alpha + 4*math.pi/3)
    y3 = 200 + radius * math.sin(alpha + 4*math.pi/3)

    arcade.draw_text("Staying safe on the Internet", 320, 710, arcade.color.BLACK, 30)
    arcade.draw_rectangle_outline(530, 720, 500, 75, arcade.color.BLACK, 5)
    arcade.draw_rectangle_outline(330, 500, 600, 282, arcade.color.BLACK, 5)
    arcade.draw_rectangle_outline(700, 200, 560, 250, arcade.color.BLACK, 5)

    arcade.draw_text("- Now that billions of people worldwide ", 67, 768-180, arcade.color.BLACK, 25)

    arcade.draw_text("have access to the internet, staying safe", 67, 768 - 210, arcade.color.BLACK, 25)

    arcade.draw_text("has never been more important.", 67, 768 - 240, arcade.color.BLACK, 25)

    arcade.draw_text("Accidentally leaking your personal ", 67, 768 - 270, arcade.color.BLACK, 25)

    arcade.draw_text("information online can be very dangerous, ", 67, 768 - 300, arcade.color.BLACK, 25)

    arcade.draw_text("and everyone should know how to avoid ", 67, 768 - 330, arcade.color.BLACK, 25)

    arcade.draw_text("this situation.", 67, 768 - 360, arcade.color.BLACK, 25)


    arcade.draw_text("- Install Anti-Virus and keep it up to date", 435, 768-492, arcade.color.BLACK, 25)
    arcade.draw_text("- Use different passwords for each site", 435, 768 - 567, arcade.color.BLACK, 25)
    arcade.draw_text("- Pay attention to the links you click", 435, 768 - 650, arcade.color.BLACK, 25)

    # arcade.draw_circle_outline(200,200,100, arcade.color.BLACK)

    texture = arcade.load_texture("Avast_alt16.png")
    scale = .1
    arcade.draw_texture_rectangle(x1, y1, scale * texture.width,
                                  scale * texture.height, texture, 0)

    texture = arcade.load_texture("windows_logos_PNG11.png")
    scale = .1
    arcade.draw_texture_rectangle(x2, y2, scale * texture.width,
                                  scale * texture.height, texture, 0)

    texture = arcade.load_texture("mcafee-antivirus-plus-test-10.png")
    scale = .2
    arcade.draw_texture_rectangle(x3, y3, scale * texture.width,
                                  scale * texture.height, texture, 0)

    texture = arcade.load_texture("58adf251e612507e27bd3c32.png")
    scale = .2
    arcade.draw_texture_rectangle(825, 768 - 266, scale * texture.width,
                                  scale * texture.height, texture, 0)

    arcade.draw_text("Click here for more information", 680, 768 - 261, arcade.color.BLACK, 20)




def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_release(x, y, button, modifiers):
    # unpack the button list into readable? variables.
    my_button_x, my_button_y, my_button_w, my_button_h = my_button

    # Need to check all four limits of the button.
    if (x > my_button_x and x < my_button_x + my_button_w and
            y > my_button_y and y < my_button_y + my_button_h):
        a_website = "https://study.com/academy/lesson/what-is-internet-security-privacy-protection-essentials.html"

        # Open url in a new window of the default browser, if possible
        webbrowser.open_new(a_website)








def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BABY_BLUE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_release = on_mouse_release

    arcade.run()


if __name__ == '__main__':
    setup()
