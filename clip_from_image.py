from colorama import init, Fore
import os.path
from moviepy.editor import *
import time


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
