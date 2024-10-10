import bpy

bl_info = {
    "name": "Anim Extensions",
    "author": "robinv",
    "version": (1, 0),
    "blender": (4, 2, 0),
    "location": "Timeline/Graph Editor/Dope Sheet -> Anim Extensions",
    "description": "Adds custom animation tools panel",
    "category": "Animation"
}


from . import utils, insert_remove_inbetween

classes = insert_remove_inbetween.classes


def register():
    utils.register()

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    utils.unregister()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

