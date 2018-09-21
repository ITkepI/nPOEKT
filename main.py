import screen,mapobject,time,sys

playscreen=screen.Screen()
map=screen.Map()

playscreen.add_element(map)

person=mapobject.DynamicObject(map, velocity=(0,1), char='$')
ground=[mapobject.DynamicObject(map, pos=(0,-1), char='_') for i in range(map.get_size()[0])]

map.add_object(person)
map.set_main(person)
for i in ground:
    map.add_object(i)

while True:
    playscreen.update()
    playscreen.print()
    time.sleep(.3)
