import bpy

from . import print_panel_values

classes = (
    print_panel_values.PrintPanelValues,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.TOPBAR_MT_help.append(print_panel_values.menu_func)
    
def unregister():
    bpy.types.TOPBAR_MT_help.remove(print_panel_values.menu_func)

    for cls in classes:
        bpy.utils.unregister_class(cls)
