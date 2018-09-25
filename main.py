import time,sys
import screen,mapobject,rendersystem, event
import DEFAULT, GLOBAL
import sdl2
from sdl2 import SDL_Color
from sdl2.sdlttf import TTF_Init

TTF_Init()

worldren=rendersystem.WorldRender()

ren=worldren.get_render()

playscreen=screen.Screen(ren)
map=screen.Map()

playscreen.add_element(map)

person=mapobject.DynamicObject(map, ren, char=b'$')

map.add_object(person)
map.set_main(person)

eventhandler=event.EventHandler()

eventhandler.add_object(person)
eventhandler.add_object(playscreen)

while not GLOBAL.gameover:
    eventhandler.event_handler()
    playscreen.update()
    worldren.present()
    time.sleep(.3)
