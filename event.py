import sdl2.ext
import sdl2
import GLOBAL

class EventHandler():
    def __init__(self):
        self.list_obj=[]
    
    def add_object(self, obj):
        self.list_obj+=[obj]
    
    def event_handler(self):
        events=sdl2.ext.get_events()
        for event in events:
            for obj in self.list_obj:
                obj.event_handler(event)
                
        
    
