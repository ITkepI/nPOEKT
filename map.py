import os
import DEFAULT

class Map:
    def __init__(self, col=DEFAULT.col, lines=DEFAULT.lines):
        self.size=(col,lines)
        self.map=[[DEFAULT.char for x in range(col)] for i in range(lines)]
        self.object_list=[]

    def cross(self, obj):
        res
        for i in self.object_list:
            if i.cross(obj):
                res=i
                break
        return res


    def get_size(self):
        return self.size

    def add_object(self,obj):
        self.object_list+=[obj]

    def update(self):
        for i in self.object_list:
            i.update()

    def set_ch(self, pos=(0,0), char=DEFAULT.char):
        self.map[pos[1]][pos[0]]=char

    def print(self):
        os.system('clear')
        for i in self.map:
            for j in i:
                print(j,end='')
            print()
        print()
