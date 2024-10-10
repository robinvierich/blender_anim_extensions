
import bpy
from bpy import context


def console_print(*args, **kwargs):
    s = str(" ".join([str(arg) for arg in args]))

    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                with bpy.context.temp_override(window=window, area=area, screen=screen):
                    bpy.ops.console.scrollback_append(text=s, type="OUTPUT")  