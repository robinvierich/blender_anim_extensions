

import bpy
from bpy.types import Panel, Operator, PropertyGroup 
from bpy.props import IntProperty

class InsertRemoveProps(PropertyGroup):
    frames: IntProperty(
        name="Frames",
        description="Number of to insert or remove",
        default=1,
        min=1,
        max=10
    ) # type: ignore


# Operators for button functionality
class ANIM_OT_button1(Operator):
    bl_idname = "anim.print_info"
    bl_label = "Print Info"
    
    def execute(self, context):
        # Add your button 1 functionality here
         # Get the current frame
        current_frame = context.scene.frame_current
        
        # Get selected keyframes
        selected_keyframes = context.selected_editable_keyframes
        
        # # Get the active action (animation data)
        # obj = context.active_object
        # if obj and obj.animation_data and obj.animation_data.action:
        #     action = obj.animation_data.action
            
        #     # Iterate through all F-Curves in the action
        #     for fcurve in action.fcurves:
        #         # Check if this F-Curve is selected in the Graph Editor
        #         if fcurve.select:
        #             # Get selected keyframes for this curve
        #             for keyframe in fcurve.keyframe_points:
        #                 if keyframe.select_control_point:
        #                     selected_keyframes.append({
        #                         'frame': int(keyframe.co[0]),
        #                         'value': keyframe.co[1],
        #                         'curve': fcurve.data_path
        #                     })
        
        # Report the findings
        self.report({'INFO'}, f"Current frame: {current_frame}")
        self.report({'INFO'}, f"Number of selected keyframes: {len(selected_keyframes)}")

        # Print detailed info about selected keyframes
        for kf in selected_keyframes:
            self.report({'INFO'}, f"Selected { str(kf.type) } at coords: { kf.co } ")

        
        return {'FINISHED'}

class ANIM_OT_button2(Operator):
    bl_idname = "anim.insert_frames"
    bl_label = "Insert Frames"
    
    def execute(self, context):
         # Add your button 1 functionality here
         # Get the current frame
        current_frame = context.scene.frame_current
        
        # Get selected keyframes
        selected_keyframes = context.selected_editable_keyframes
        
        frames = context.scene.insert_remove_props.frames

        # Print detailed info about selected keyframes
        for kf in selected_keyframes:
            if kf.co_ui.x >= current_frame:
                kf.co_ui.x += frames

        
        return {'FINISHED'}

class ANIM_OT_button3(Operator):
    bl_idname = "anim.remove_frames"
    bl_label = "Remove Frames"
    
    def execute(self, context):
        current_frame = context.scene.frame_current
        selected_keyframes = context.selected_editable_keyframes
        
        frames = context.scene.insert_remove_props.frames

        # Print detailed info about selected keyframes
        for kf in selected_keyframes:
            if kf.co_ui.x >= current_frame:
                kf.co_ui.x -= frames

        return {'FINISHED'}


CATEGORY = "Anim Extensions"
MENU_LABEL = "Anim Extensions"

class InsertRemoveInbetweenPanel(Panel):
    bl_category = CATEGORY
    bl_label = MENU_LABEL

    # @classmethod
    # def poll(cls, context):
    #     return context.area.type == 'DOPESHEET_EDITOR' or context.area.type == 'GRAPH_EDITOR'

    def draw(self, context):
        layout = self.layout

        layout.operator("anim.print_info")

        layout.operator("anim.insert_frames")
        layout.operator("anim.remove_frames")
         # Add frames input field
        layout.prop(context.scene.insert_remove_props, "frames")

# # Panel for Timeline
# class ANIM_PT_verset_timeline(InsertRemoveInbetweenPanel):
#     bl_space_type = 'DOPESHEET_EDITOR'
#     bl_region_type = 'UI'
    
#     @classmethod
#     def poll(cls, context):
#         return context.area.type == 'DOPESHEET_EDITOR' and context.space_data.mode == 'TIMELINE'
    
# Panel for Graph Editor
class ANIM_PT_verset_graph(InsertRemoveInbetweenPanel):
    bl_space_type = 'GRAPH_EDITOR'
    bl_region_type = 'UI'


# Panel for Dope Sheet
class ANIM_PT_verset_dopesheet(InsertRemoveInbetweenPanel):
    bl_space_type = 'DOPESHEET_EDITOR'
    bl_region_type = 'UI'


# Registration
classes = (
    ANIM_OT_button1,
    ANIM_OT_button2,
    ANIM_OT_button3,
    # ANIM_PT_verset_timeline,
    ANIM_PT_verset_graph,
    ANIM_PT_verset_dopesheet
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

