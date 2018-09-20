import map,mapobject,time,sys

map=map.Map()
person=mapobject.DynamicObject(map, velocity=(0,1), char='$')
ground=[mapobject.DynamicObject(map, pos=(0,-1), char='_') for i in range(map.get_size()[0])]



map.add_object(person)
for i in ground:
    map.add_object(i)

while True:
    map.update()
    map.print()
    time.sleep(.3)
