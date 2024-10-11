
from bpy.types import Context

def get_selected_keyframes(context : Context):
    if context.area.type == 'DOPESHEET_EDITOR':
        obj = context.active_object
        action = obj.animation_data.action if obj and obj.animation_data else None

        if not action:
            return []

        all_keyframes = []

        for fcurve in action.fcurves: 
            all_keyframes.extend(fcurve.keyframe_points.values())

        all_selected_keyframes = [keyframe for keyframe in all_keyframes if keyframe.select_control_point]

        return all_selected_keyframes

    elif context.area.type == 'GRAPH_EDITOR':
        return context.selected_editable_keyframes
    
    return []

def get_scene_keyframes(context : Context):
    all_keyframes = []
    for obj in context.scene.objects:
        action = obj.animation_data.action if obj and obj.animation_data else None

        if not action:
            return []

        for fcurve in action.fcurves: 
            all_keyframes.extend(fcurve.keyframe_points.values())

    return all_keyframes