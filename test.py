from moviepy.editor import *

clip = VideoFileClip("VID_20220928_111008.mp4")
clip = clip.rotate(45)
clip.write_videofile("1.mp4")