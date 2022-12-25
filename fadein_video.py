from moviepy.editor import *


def fadein_video(path_to_file, output_file_name, time):
    clip = VideoFileClip(path_to_file)
    clipColorx = clip.fx(vfx.fadein, time)
    clipColorx.write_videofile(output_file_name)
