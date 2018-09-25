import screen, rendersystem, GLOBAL
import sdl2.ext
import sdl2

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

    def event_handler(self):
        pass

    def key_handler_onpress(self, key_name):
        pass

    def key_handler_release(self, key_name):
        pass

    def update_pos(self):
        pass

    def update(self):
        pass

class DynamicObject(MapObject):
    def __init__(self, map, render, pos=(0,0), char=b'H', color=sdl2.SDL_Color(0,0,0), velocity=(0,0)):
        super().__init__(map, pos)
        tex=rendersystem.load_texture_from_text(char, render, color=color)
        self.rensys=rendersystem.RenderSystem(tex, render)
        self.velocity=velocity
        self.char=char

    def move(self, delta=(0,0)):
        pos_x=self.pos[0]+delta[0]
        pos_y=self.pos[1]+delta[1]
        self.pos=(pos_x,pos_y)

    def move_to(self, pos=(0,0)):
        self.pos=pos

    def update_pos(self):
        self.move(self.velocity)

    def event_handler(self, event):
        if event.type==sdl2.SDL_KEYDOWN:
            self.key_handler_onpress(event.key.keysym.sym)
        if event.type==sdl2.SDL_KEYUP:
            self.key_handler_release(event.key.keysym.sym)

    def key_handler_onpress(self, key_name):
        for key, value in GLOBAL.control_keys.items():
            if key_name==value:
                if key=='UP':
                    self.move((0,-1))
                    break
                elif key=='DOWN':
                    self.move((0,1))
                    break
                elif key=='LEFT':
                    self.move((-1,0))
                    break
                elif key=='RIGHT':
                    self.move((1,0))
                    break

    def update(self):
        self.update_pos()
        self.rensys.render(pos=self.pos)





class BigObject(MapObject):
    def __init__(self, map, pos=(0,0), object_list=[]):
        MapObject.__init__(map,pos)

