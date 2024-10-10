import bpy
from bpy.types import Panel, Operator
from collections import defaultdict

import inspect

from bpy import context

import builtins as __builtin__

def console_print(*args, **kwargs):
    s = str(" ".join([str(arg) for arg in args]))

    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                with bpy.context.temp_override(window=window, area=area, screen=screen):
                    bpy.ops.console.scrollback_append(text=s, type="OUTPUT")  


def print(*args, **kwargs):
    """Console print() function."""

    console_print(*args, **kwargs) # to py consoles
    __builtin__.print(*args, **kwargs) # to system console

def all_panels():
    for prop in dir(bpy.types):
        cls = getattr(bpy.types, prop)
        if inspect.isclass(cls) and issubclass(cls, Panel):
            yield cls

class PrintPanelValues(Operator):
    bl_idname = "verset.print_panel_values"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Print Panel Values"         # Display name in the interface.

    def execute(self, context):
        attrs = ["bl_space_type", "bl_region_type", "bl_context"]
        options = defaultdict(lambda: set())

        for panel in all_panels():
            for attr in attrs:
                if hasattr(panel, attr):
                    value = getattr(panel, attr)
                    options[attr].add(value)
                
        for opt, values in options.items():
            print(60*"-")
            print(opt)
            print(values)
        
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(PrintPanelValues.bl_idname)


def register():
    bpy.utils.register_class(PrintPanelValues)
    bpy.types.TOPBAR_MT_help.append(menu_func)

def unregister():
    bpy.types.TOPBAR_MT_help.remove(menu_func)
    bpy.utils.unregister_class(PrintPanelValues)
