import unittest
from pathlib import Path
from video_speed import video_speed
from moviepy.editor import VideoFileClip, AudioFileClip
from main import create_file_name
from fadein_video import fadein_video
from fadeout_video import fadeout_video
from rotate_video import rotate_video


class VideoEditorTests(unittest.TestCase):
    def setUp(self):
        self.test_video = str(Path("test_folder\\VID_20220928_111008.mp4").absolute())
        self.output_video = str(Path("test_folder\\VID_20220928_111008(out).mp4").absolute())

    def test_video_speed_x2(self):
        speed_factor = 2
        video_speed(self.test_video, self.output_video, speed_factor)
        clip = VideoFileClip(self.test_video)
        clip_x2 = VideoFileClip(self.output_video)

        actual = clip_x2.duration
        expected = clip.duration / speed_factor

        self.assertAlmostEqual(actual, expected, 1)

    def test_video_speed_audio_x2(self):
        speed_factor = 2
        video_speed(self.test_video, self.output_video, speed_factor)
        audio = AudioFileClip(self.test_video)
        audio_x2 = AudioFileClip(self.output_video)

        actual = audio_x2.duration
        expected = audio.duration / speed_factor

        self.assertAlmostEqual(actual, expected, 1)

    def test_with_wrong_file(self):
        speed_factor = 2
        test_video = str(Path("test_folder\\VID_20220928_11100.mp4").absolute())
        self.assertRaises(OSError, video_speed, test_video, self.output_video, speed_factor)

    def test_with_wrong_speed_factor(self):
        speed_factor = -1
        self.assertRaises(ValueError, video_speed, self.test_video, self.output_video, speed_factor)

    def test_create_file_name(self):
        path_dir = Path("video-editor\\test_folder").absolute()
        file_name = create_file_name(path_dir, 10, '.mp4')
        file_name2 = create_file_name(path_dir, 10, '.mp4')
        self.assertNotEqual(file_name, file_name2)

    def test_fadein_video(self):
        fadein_video(self.test_video, self.output_video, 2)
        speed1 = VideoFileClip(self.test_video).duration
        speed2 = VideoFileClip(self.output_video).duration
        self.assertAlmostEqual(speed1, speed2, 1)

    def test_fadeout_video(self):
        fadeout_video(self.test_video, self.output_video, 2)
        speed1 = VideoFileClip(self.test_video).duration
        speed2 = VideoFileClip(self.output_video).duration
        self.assertAlmostEqual(speed1, speed2, 1)

    def test_rotate_video(self):
        rotate_video(self.test_video, self.output_video, 45)
        speed1 = VideoFileClip(self.test_video).duration
        speed2 = VideoFileClip(self.output_video).duration
        self.assertAlmostEqual(speed1, speed2, 1)

    def test_rotate_video2(self):
        self.assertRaises(TypeError, rotate_video, self.test_video, self.output_video, "45")

    def test_fadeout_video2(self):
        fadeout_video(self.test_video, self.output_video, -1)
        speed1 = VideoFileClip(self.test_video).duration
        speed2 = VideoFileClip(self.output_video).duration
        self.assertAlmostEqual(speed1, speed2, 1)

    def test_fadein_video2(self):
        self.assertRaises(TypeError, fadein_video, self.test_video, self.output_video, "2")






if __name__ == "__main__":
    unittest.main()
