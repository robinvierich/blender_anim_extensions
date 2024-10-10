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


def register():
    utils.register()
    insert_remove_inbetween.register()


def unregister():
    utils.unregister()
    insert_remove_inbetween.unregister()

