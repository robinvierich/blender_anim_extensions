

import bpy
from bpy.types import Panel, Operator, PropertyGroup 
from bpy.props import IntProperty

from utils.keyframe_utils import get_selected_keyframes

class InsertRemoveProps(PropertyGroup):
    frames: IntProperty(
        name="Frames",
        description="Number of to insert or remove",
        default=1,
        min=1,
        max=10
    ) # type: ignore


# Operators for button functionality
class ANIM_OT_PrintInfo(Operator):
    bl_idname = "anim.print_info"
    bl_label = "Print Info"
    
    def execute(self, context):
        current_frame = context.scene.frame_current
        selected_keyframes = get_selected_keyframes(context)
        
        self.report({'INFO'}, f"Current frame: {current_frame}")
        self.report({'INFO'}, f"Number of selected keyframes: {len(selected_keyframes)}")

        for kf in selected_keyframes:
            self.report({'INFO'}, f"Selected { str(kf.type) } at coords: { kf.co } ")

        
        return {'FINISHED'}


class ANIM_OT_InsertInbetween(Operator):
    bl_idname = "anim.insert_inbetween"
    bl_label = "Insert Frames"
    
    def execute(self, context):
        current_frame = context.scene.frame_current
        selected_keyframes = get_selected_keyframes(context)
        
        frames = context.scene.insert_remove_props.frames

        for kf in selected_keyframes:
            if kf.co_ui.x >= current_frame:
                kf.co_ui.x += frames

        
        return {'FINISHED'}


class ANIM_OT_RemoveInbetween(Operator):
    bl_idname = "anim.remove_inbetween"
    bl_label = "Remove Frames"
    
    def execute(self, context):
        current_frame = context.scene.frame_current
        selected_keyframes = get_selected_keyframes(context)
        
        frames = context.scene.insert_remove_props.frames

        for kf in selected_keyframes:
            if kf.co_ui.x >= current_frame:
                kf.co_ui.x -= frames

        return {'FINISHED'}


CATEGORY = "Anim Extensions"
MENU_LABEL = "Anim Extensions"

class ANIM_PT_InsertRemoveInbetween(Panel):
    bl_category = CATEGORY
    bl_label = MENU_LABEL

    def draw(self, context):
        layout = self.layout

        layout.operator("anim.print_info")

        layout.operator("anim.insert_inbetween")
        layout.operator("anim.remove_inbetween")
         # Add frames input field
        layout.prop(context.scene.insert_remove_props, "frames")


# Panel for Graph Editor
class ANIM_PT_InsertRemoveInBetween_graph(ANIM_PT_InsertRemoveInbetween):
    bl_space_type = 'GRAPH_EDITOR'
    bl_region_type = 'UI'


# Panel for Dope Sheet
class ANIM_PT_InsertRemoveInBetween_dopesheet(ANIM_PT_InsertRemoveInbetween):
    bl_space_type = 'DOPESHEET_EDITOR'
    bl_region_type = 'UI'


# Registration
classes = (
    ANIM_OT_PrintInfo,
    ANIM_OT_InsertInbetween,
    ANIM_OT_RemoveInbetween,
    ANIM_PT_InsertRemoveInBetween_graph,
    ANIM_PT_InsertRemoveInBetween_dopesheet
)


import bpy

def register():
    bpy.utils.register_class(InsertRemoveProps)
    bpy.types.Scene.insert_remove_props = bpy.props.PointerProperty(type=InsertRemoveProps)

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    bpy.utils.unregister_class(InsertRemoveProps)
    del bpy.types.Scene.insert_remove_props 

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
