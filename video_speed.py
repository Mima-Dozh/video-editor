from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx


def video_speed(in_loc, out_loc, speed_factor):
    # Import video clip
    clip = VideoFileClip(in_loc)
    print("fps: {}".format(clip.fps))

    # Modify the FPS
    clip = clip.set_fps(clip.fps * int(speed_factor))

    # Apply speed up
    final = clip.fx(vfx.speedx, int(speed_factor))
    print("fps: {}".format(final.fps))

    # Save video clip
    final.write_videofile(out_loc)