from moviepy.editor import *


def fadeout_video(path_to_file, output_file_name, time):
    clip = VideoFileClip(path_to_file)
    clipColorx = clip.fx(vfx.fadeout, time)
    clipColorx.write_videofile(output_file_name)
