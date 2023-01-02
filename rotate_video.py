from moviepy.editor import *

def rotate_video(in_loc, out_loc, angle):
    clip = VideoFileClip(in_loc)
    clip = clip.rotate(angle)
    clip.write_videofile(out_loc)