import time,sys
import screen,mapobject,rendersystem
import DEFAULT

worldren=rendersystem.WorldRender()

ren=worldren.get_render()

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
    worldren.present()
    time.sleep(.3)
