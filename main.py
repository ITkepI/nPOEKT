import time,sys
from sdl2 import *
import screen,mapobject,rendersystem
import DEFAULT

win = SDL_CreateWindow(b"Hello World",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              *DEFAULT.size, SDL_WINDOW_SHOWN)
			      
ren=SDL_CreateRenderer(win, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)


tex=rendersystem.load_texture_from_image(b"resources/hello.bmp",ren)

screenrensys=rendersystem.RenderSystem(tex, ren)
screenrensys.render(full=True)
playscreen=screen.Screen(screenrensys)
map=screen.Map()

playscreen.add_element(map)
#playscreen.update()

personrensys=rendersystem.RenderSystem(rendersystem.load_texture_from_image(b"resources/HalfOgreFighter3.png", ren), ren)

person=mapobject.DynamicObject(map, personrensys, velocity=(0,1), char='$')

map.add_object(person)
map.set_main(person)

while True:
    playscreen.update()
    SDL_RenderPresent(ren)
    time.sleep(.3)
