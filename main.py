import pygame as pg
import constants as c
from tool import Tool
from canvas import Canvas
from button import Button

pg.init()

#create a font
my_font = pg.font.SysFont('Comic Sans MS', 50)
plus = my_font.render('+', False, (0, 0, 0))
minus = my_font.render('-', False, (0, 0, 0))

#create clock
clock = pg.time.Clock()

screen = pg.display.set_mode((c.WINDOW_WIDTH + 150, c.WINDOW_HEIGHT))
pg.display.set_caption("Draw")

#creat canvas
canvas_image = pg.Surface((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
canvas = Canvas(canvas_image)

#create buttons
button_up_image = pg.Surface((30, 30))
button_down_image = pg.Surface((30, 30))
button_canvas_color_image = pg.Surface((60, 30))
button_up = Button(c.WINDOW_WIDTH + 20, 10, button_up_image, "red")
button_down = Button(c.WINDOW_WIDTH + 100, 10, button_down_image, "blue")
button_canvas_color = Button(c.WINDOW_WIDTH + 20, 100, button_canvas_color_image, "black")

#create tool image
tool_size = 16
tool_image = pg.Surface((tool_size, tool_size))
tool = Tool(tool_image, (50, 50), tool_size)

#sprite groups
player_group = pg.sprite.Group()

run = True
while run:

    clock.tick(c.FPS)

    screen.fill("grey100")

    for event in pg.event.get():
        #quit programm
        if event.type == pg.QUIT:
            run = False
    #mouse click
        if pg.mouse.get_pressed()[0]:
            mouse_pos = pg.mouse.get_pos()
            tool = Tool(tool_image, mouse_pos, tool_size)
            #if mouse goes into the siedbar
            if mouse_pos[0] < c.WINDOW_WIDTH - (tool_size/2):
                player_group.add(tool)

    #draw
    canvas.draw(screen)
    player_group.draw(screen)

    #draw buttons
    if button_up.draw(screen):
        tool_size += 4
        tool_image = pg.Surface((tool_size, tool_size))
        tool.update_size(tool_image, tool_size)
    elif button_down.draw(screen):
        tool_size -= 4
        tool_image = pg.Surface((tool_size, tool_size))
        tool.update_size(tool_image, tool_size)
    button_canvas_color.draw(screen)


    screen.blit(plus, (c.WINDOW_WIDTH + 26, 6))
    screen.blit(minus, (c.WINDOW_WIDTH + 110, 6))
    screen.blit(my_font.render(f'Size: {int(tool_size/4)}', False, (0, 0, 0)), (c.WINDOW_WIDTH + 10, 50))

    #update
    tool.update(screen)

    #update display
    pg.display.flip()

pg.quit()