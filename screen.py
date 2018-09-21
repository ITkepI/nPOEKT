import os
import DEFAULT
import terminal

class Screen:
    def __init__(self,size=DEFAULT.size):
        self.render_list=[]

    def add_element(self,el):
        self.render_list+=[el]

    def update(self):
        for i in self.render_list:
            i.update()

    def print(self):
        for i in self.render_list:
            i.print()

class ScreenElement():
    """docstring for ScreenElement"""
    def update(self):
        pass

    def print(self):
        pass


class Map(ScreenElement):
    def __init__(self, col=DEFAULT.col, lines=DEFAULT.lines):
        self.size=(col,lines)
        self.map=[[DEFAULT.char for x in range(lines)] for i in range(col)]
        self.object_list=[]
        self.center=(col/2, lines/2)
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

    def print(self):
        os.system('clear')
        self.update_center(self.main_person.get_pos())
        terminal_size=terminal.get_terminal_size()
        bottom=0
        top=self.size[1]-1
        left=0
        right=self.size[0]-1
        if self.size[1]>terminal_size[1]:
            top=int(self.center[1]+terminal_size[1]/2)
            bottom=int(self.center[1]-terminal_size[1]/2)
        if self.size[0]>terminal_size[0]:
            right=int(self.center[0]+terminal_size[0]/2)
            left=int(self.center[0]-terminal_size[0]/2)

        if bottom<0:
            bottom=0

        if left<0:
            left=0

        for y in range(bottom,top):
            for x in range(left,right):
                print(self.map[x][y],end='')
            print()
        '''for i in self.map:
            for j in i:
                print(j,end='')
            print()
        print()'''
