import bpy
from bpy.props import FloatProperty, IntProperty, EnumProperty


class MESH_OT_bevel_cmd(bpy.types.Operator):
    bl_idname = "mesh.bevel_cmd"
    bl_label = "Bevel Command"
    bl_options = {'REGISTER', 'UNDO'}

    # ✅ Properties (F9 panel + popup ke liye)
    width: FloatProperty(
        name="Width",
        default=0.1,
        min=0.0
    )

    segments: IntProperty(
        name="Segments",
        default=1,
        min=1
    )

    affect: EnumProperty(
        name="Affect",
        items=[
            ('EDGES', "Edges", ""),
            ('VERTICES', "Vertices", "")
        ],
        default='EDGES'
    )

    # ✅ Main logic
    def execute(self, context):
        bpy.ops.mesh.bevel(
            offset=self.width,
            segments=self.segments,
            affect=self.affect
        )
        return {'FINISHED'}

    # ✅ Popup (optional but PRO)
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    # ✅ UI layout (popup ka design)
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "width")
        layout.prop(self, "segments")
        layout.prop(self, "affect")


# ✅ Clean register system
classes = [
    MESH_OT_bevel_cmd,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)