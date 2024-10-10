
ADDON_NAME = "Verset Anim Extensions"

bl_info = {
    "name": ADDON_NAME,
    "author": "robinv",
    "version": (1, 0),
    "blender": (4, 2, 0),
    "location": "Timeline/Graph Editor/Dope Sheet -> Verset Anim Extensions",
    "description": "Adds custom animation tools panel",
    "category": "Animation"
}

import bpy
from bpy.types import Panel, Operator


# Operators for button functionality
class ANIM_OT_button1(Operator):
    bl_idname = "anim.custom_button1"
    bl_label = "Button 1"
    
    def execute(self, context):
        # Add your button 1 functionality here
        self.report({'INFO'}, "Button 1 pressed!")
        return {'FINISHED'}

class ANIM_OT_button2(Operator):
    bl_idname = "anim.custom_button2"
    bl_label = "Button 2"
    
    def execute(self, context):
        # Add your button 2 functionality here
        self.report({'INFO'}, "Button 2 pressed!")
        return {'FINISHED'}

class ANIM_OT_button3(Operator):
    bl_idname = "anim.custom_button3"
    bl_label = "Button 3"
    
    def execute(self, context):
        # Add your button 3 functionality here
        self.report({'INFO'}, "Button 3 pressed!")
        return {'FINISHED'}


CATEGORY = "Verset Anim Extensions"
MENU_LABEL = "Verset Anim Extensions"

# Panel for Timeline
class ANIM_PT_verset_timeline(Panel):
    bl_space_type = 'DOPESHEET_EDITOR'
    bl_region_type = 'UI'
    bl_category = CATEGORY
    bl_label = MENU_LABEL
    
    @classmethod
    def poll(cls, context):
        return context.area.type == 'DOPESHEET_EDITOR' and context.space_data.mode == 'TIMELINE'
    
    def draw(self, context):
        layout = self.layout
        layout.operator("anim.custom_button1")
        layout.operator("anim.custom_button2")
        layout.operator("anim.custom_button3")

# Panel for Graph Editor
class ANIM_PT_verset_graph(Panel):
    bl_space_type = 'GRAPH_EDITOR'
    bl_region_type = 'UI'
    bl_category = CATEGORY
    bl_label = MENU_LABEL
    
    def draw(self, context):
        layout = self.layout
        layout.operator("anim.custom_button1")
        layout.operator("anim.custom_button2")
        layout.operator("anim.custom_button3")

# Panel for Dope Sheet
class ANIM_PT_verset_dopesheet(Panel):
    bl_space_type = 'DOPESHEET_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Custom Animation Tools'
    bl_label = "Custom Animation Tools"
    
    @classmethod
    def poll(cls, context):
        return context.area.type == 'DOPESHEET_EDITOR' and context.space_data.mode == 'ACTION'
    
    def draw(self, context):
        layout = self.layout
        layout.operator("anim.custom_button1")
        layout.operator("anim.custom_button2")
        layout.operator("anim.custom_button3")

# Registration
classes = (
    ANIM_OT_button1,
    ANIM_OT_button2,
    ANIM_OT_button3,
    ANIM_PT_verset_timeline,
    ANIM_PT_verset_graph,
    ANIM_PT_verset_dopesheet
)

import bpy
from bl_operators.presets import AddPresetBase


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
