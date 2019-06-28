#!/usr/bin/python
# -*- coding: utf-8 -*-

import bpy, bmesh


class MHC_OT_CheckVGroupsOperator(bpy.types.Operator):
    """Extract one helper vertex group as clothes"""
    bl_idname = "makeclothes.check_vertex_groups"
    bl_label = "Check vertex groups"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(self, context):
        if context.active_object is not None:
            if not hasattr(context.active_object, "MhObjectType"):
                return False
            if context.active_object.select_get():
                if context.active_object.MhObjectType == "Clothes":
                    return True
        return False

    def execute(self, context):
        self.report({'INFO'}, "Seems OK")
        return {'FINISHED'}