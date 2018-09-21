import screen

class MapObject:
    def __init__(self, map, pos=(0,0)):
        self.pos=pos
        self.map=map

    def get_pos(self):
        return self.pos

    def cross(self, obj):
        if obj.pos==self.pos:
            return True
        else:
            return False

    def key_handler_onpress(self, key_name):
        pass

    def key_handler_release(self, key_name):
        pass

    def update_pos(self):
        pass

    def update(self):
        pass

class DynamicObject(MapObject):
    def __init__(self, map, pos=(0,0), char='H', velocity=(0,0)):
        super().__init__(map, pos)
        self.velocity=velocity
        self.char=char

    def update_pos(self):
        pos_x=self.pos[0]+self.velocity[0]
        pos_y=self.pos[1]+self.velocity[1]
        self.pos=(pos_x,pos_y)

    def update(self):
        self.map.set_ch(self.pos)
        self.update_pos();
        self.map.set_ch(self.pos, self.char)

class BigObject(MapObject):
    def __init__(self, map, pos=(0,0), object_list=[]):
        MapObject.__init__(map,pos)

