from colorama import init, Fore
import os.path
from moviepy.editor import *
import time
from numpy import arange


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
                video.save_frame(os.path.join(os.path.split(path_file)[0], vid_name, f'{vid_name}_{clip}.jpg'), clip)
            print(Fore.GREEN + f'\n[+] Кадры из видео сохранены в папку: "{os.path.join(os.path.split(path_file)[0], vid_name)}"')
            return
        else:
            print(Fore.RED + '[-] Неверное расширение файла')
            return
    else:
        print(Fore.RED + '[-] Указанного видео не существует')
        return
