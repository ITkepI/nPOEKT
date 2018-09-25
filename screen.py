import os
import DEFAULT
import terminal
import rendersystem
import sys, sdl2

class Screen:
    def __init__(self, render, background_path=b"resources/back.png", size=DEFAULT.size):
        tex=rendersystem.load_texture_from_image(background_path, render)
        self.rendersys=rendersystem.RenderSystem(tex,render)
        self.render_list=[]

    def add_element(self,el):
        self.render_list+=[el]

    def update(self):
        #self.event_handler(sdl2.SDL_QUIT)
        self.rendersys.render(full=True)
        for i in self.render_list:
            i.update()

    def print(self):
        for i in self.render_list:
            i.print()
    
    def event_handler(self, event):
        if event.type==sdl2.SDL_QUIT:
            sdl2.SDL_Quit()
            sys.exit()

class ScreenElement():
    """docstring for ScreenElement"""
    def update(self):
        pass

    def print(self):
        pass


class Map(ScreenElement):
    def __init__(self, size=DEFAULT.size):
        self.size=size
        self.object_list=[]
        self.center=(size[0]/2, size[1]/2)
        self.main_person=None

    def set_main(self, person):
        self.main_person=person

    def cross(self, obj):
        res
        for i in self.object_list:
            if i.cross(obj):
                res=i
                break
        return res

    def update_center(self,pos=(0,0)):
        self.center=pos

    def get_size(self):
        return self.size

    def add_object(self,obj):
        self.object_list+=[obj]

    def update(self):
        for i in self.object_list:
            i.update()

    def set_ch(self, pos=(0,0), char=DEFAULT.char):
        self.map[pos[0]][pos[1]]=char
