import sys, os
import ctypes
from sdl2 import *
from sdl2.sdlttf import *
import sdl2.sdlimage

class RenderSystem:
    def __init__(self, tex, ren):
        self.tex=tex
        self.ren=ren
    
    def render(self, size=1, pos=(0,0), full=False):
        if full:
            SDL_RenderCopy(self.ren, self.tex, None, None)
            return
        dst=SDL_Rect()
        dst.x, dst.y = pos
        w=ctypes.c_int()
        h=ctypes.c_int()
        if size==None:
            SDL_QueryTexture(self.tex, None, None, w, h)
        else:
            w, h = size*8, size*12
        dst.w, dst.h = w, h
        SDL_RenderCopy(self.ren, self.tex, None, dst) 

def load_texture_from_image(image_path, ren):
    bmp=sdl2.sdlimage.IMG_Load(image_path)
    tex=SDL_CreateTextureFromSurface(ren, bmp)
    SDL_FreeSurface(bmp)
    return tex
    
    
def load_texture_from_text(message, renderer, fontFile=b"open-sans/OpenSans-Bold.ttf", color=SDL_Color(255,255,255), fontSize=10):
    """

    :rtype : SDL_Texture
    """
    # Open the font
    SDL_ClearError()
    fontsize=ctypes.c_int()
    fontsize=fontSize
    font = TTF_OpenFont(fontFile, fontSize)

    #We need to first render to a surface as that's what TTF_RenderText
    #returns, then load that surface into a texture
    surf = TTF_RenderText_Blended(font, message, color)

    if surf is None:
        TTF_CloseFont(font)
        print("TTF_RenderText")
        return None

    texture = SDL_CreateTextureFromSurface(renderer, surf)
    if texture is None:
        print("CreateTexture")

    #Clean up the surface and font
    SDL_FreeSurface(surf)
    TTF_CloseFont(font)
    return texture

