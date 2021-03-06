from pygame.image import load
from pygame.mixer import Sound


def load_sprite(name: str, with_alpha: bool = True):
    """
    Loads a sprite given the name. This will build a path to the sprite and load it

    """
    # You can find a better way for the extension for the asset to be added
    # this uses .png assets
    path = f"assets/sprites/{name}.png"

    # returns a Surface (https://www.pygame.org/docs/ref/surface.html) 
    # that can be used to represent images which can be used to
    # draw on the screen
    loaded_sprite = load(path)

    # converts the image to either be transparent or not.
    # Generally, you could just use convert_alpha() for all types of images since it can also handle an image without
    # transparent pixels.
    # However, drawing transparent images is a bit slower than drawing nontransparent ones.
    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()


def load_sound(name):
    path = f"assets/sounds/{name}.wav"
    return Sound(path)
