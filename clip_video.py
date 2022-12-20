from colorama import init, Fore
import os.path
from moviepy.editor import *
import time


def clip_video(path_file, start_time, end_time):
    if os.path.isfile(path_file):
        if os.path.split(path_file)[-1].endswith(".mp4") or os.path.split(path_file)[-1].endswith(".avi"):
            dir_vid = os.path.split(path_file)[0]
            suff = f'.{os.path.split(path_file)[-1].split(".")[-1]}'
            vid_clip_name = f'{os.path.split(path_file)[-1].removesuffix(suff)}_clip{suff}'

            try:
                start = int(start_time.split(":")[0]) * 60 + int(start_time.split(":")[1])
            except IndexError:
                start = int(start_time)
            except ValueError:
                print(Fore.RED + '[-] Вы ввели не число')
                return
            try:
                end = int(end_time.split(":")[0]) * 60 + int(end_time.split(":")[1])
            except IndexError:
                end = int(end_time)
            except ValueError:
                print(Fore.RED + '[-] Вы ввели не число')
                return

            print(Fore.CYAN + '[+] Начинаю вырезку фрагмента видео')
            print(Fore.YELLOW + f'   - Длительность фрагмента: {end - start} секунд')

            clip = VideoFileClip(path_file)
            print(Fore.YELLOW + f'   - Общая продолжительность видео: {clip.duration} секунд\n')

            clip_clip = clip.subclip(start, end)
            print(Fore.CYAN + '[+] Записываю фрагмент видео...\n')
            clip_clip.write_videofile(os.path.join(dir_vid, f'{vid_clip_name}'))
            clip.reader.close()
            clip.audio.reader.close_proc()
            print(Fore.GREEN + f'\n[+] Видео сохранено в папку: "{os.path.join(dir_vid, f"{vid_clip_name}")}"')
            return
        else:
            print(Fore.RED + '[-] Файл не поддерживаемого формата')
            return
    else:
        print(Fore.RED + '[-] Не указан файл')
        return
