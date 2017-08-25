import bpy

scene = bpy.context.scene
old = scene.render.filepath 
scene.render.image_settings.file_format = 'PNG' 

for frame_nr in range(1, 359):
    scene.frame_set(frame_nr)
    absPath = "/Users/jyu/CS/CS6475/project/blender_source/"
    scene.render.filepath = absPath + str(frame_nr)
    scene.render.alpha_mode = 'RED'
    bpy.ops.render.render(write_still=True) 

# restore the filepath
scene.render.filepath = old