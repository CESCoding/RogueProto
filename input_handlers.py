import tcod as libtcod

def handle_keys(key):
    if key.vk == libtcod.KEY_UP:
        return {'move':(0,-1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move':(0,1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move':(-1,0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move':(1,0)}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt + Enter: toggle fullscreen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}