import os.path
import time
from numpy import arange

from colorama import Fore
from colorama import init
from moviepy.editor import *

init()


def extract_image_from_video(path_file):
    if os.path.exists(path_file):
        suff = f'.{os.path.split(path_file)[-1].split(".")[-1]}'
        vid_name = f'{os.path.split(path_file)[-1].removesuffix(suff)}'
        if path_file.endswith(".mp4") or path_file.endswith(".avi"):
            print(Fore.CYAN + '[+] Сохранение кадров из видео')
            if not os.path.isdir(os.path.join(os.path.split(path_file)[0], vid_name)):
                os.mkdir(os.path.join(os.path.split(path_file)[0], vid_name))

            video = VideoFileClip(path_file)
            s_fps = (1 / video.fps) * 10
            for clip in arange(0, video.duration, s_fps):
                print(Fore.YELLOW + f'\r[+] Сохраняю: {clip}/{video.duration}', end='')
                video.save_frame(os.path.join(os.path.split(path_file)[0], 
                                              vid_name, 
                                              f'{vid_name}_{clip}.jpg'), 
                                 clip)
            print(Fore.GREEN + f'\n[+] Кадры из видео сохранены в папку: '
                               f'"{os.path.join(os.path.split(path_file)[0], vid_name)}"')
            return
        else:
            print(Fore.RED + '[-] Неверное расширение файла')
            return
    else:
        print(Fore.RED + '[-] Указанного видео не существует')
        return


def clip_from_image(path_dir, name_clip, s_duration):
    try:
        dur = float(s_duration)
    except ValueError:
        print(Fore.RED + '[-] Неверное значение длительности кадра')
        return

    if os.path.exists(path_dir):
        print(Fore.CYAN + '[+] Создание видео из картинок')
        os.chdir(path_dir)
        images = list(filter(lambda img: img.endswith(".jpg"), os.listdir(path_dir)))
        
        clips = [ImageClip(im).set_duration(dur) for im in images]
        video_merge = concatenate_videoclips(clips, method='compose')
        video_merge.write_videofile(f'{name_clip}.mp4', fps=25)
        print(Fore.GREEN + f'[+] Видео создано и сохранено в папку: {path_dir}')
        return
    else:
        print(Fore.RED + '[-] Указанной директории не существует')
        return


path_file = "D:\\py\\py.Task\\video-editor\\VID_20221101_213727.mp4"
path_dir = "D:\\py\\py.Task\\video-editor\\VID_20221101_213727"
name = "VID_20221101_213727"

extract_image_from_video(path_file)
clip_from_image(path_dir, name, 0.5)
