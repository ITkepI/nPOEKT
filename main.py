import map,mapobject,time,event

map=map.Map()
person=mapobject.MapObject(map, velocity=(0,1), char='$')
ground=[mapobject.MapObject(map, pos=(0,-1), char='_') for i in range(map.get_size()[0])]



map.add_object(person)
for i in ground:
    map.add_object(i)
while True:
    map.update()
    map.print()
    time.sleep(.3)
