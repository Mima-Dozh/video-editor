import argparse
import os
from colorama import init, Fore
from merge_videos import merge_videos
from clip_video import clip_video
from extract_image_from_video import extract_image_from_video
from video_speed import video_speed
from clip_from_image import clip_from_image
import tempfile
from pathlib import Path
import shutil

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED


def main():
    with tempfile.TemporaryDirectory(dir = Path()) as tmpdirname:
        i = 0
        path_dir = Path(tmpdirname)
        while True:
            i += 1
            user_change = input(RESET + '\n[+] Выберите действие:\n\t[1] Объединить видео\n\t[2] Вырезать фрагмент\n\t'
                                '[3] Извлечь кадры из видео\n\t[4] Создать клип из картинок\n\t'
                                '[5] Изменить скорость видео\n\t[6] Сохранить изменения\n\t[7] Отменить изменения\n\t[8] Выход\n>>> ')
            if user_change == "1":
                merge_videos(input('\n[+] Введите путь к папке с файлами: '),
                             str(path_dir/(str(i) + '.mp4')))
            elif user_change == "2":
                clip_video(input('\n[+] Введите путь к файлу видео: '), input('[+] Введите время начала фрагмента\n'
                                                                              '   - пример: 02:25\n   >>> '),
                           input('[+] Введите время окончания фрагмента\n'
                                 '   - пример: 03:50\n   >>> '))
            elif user_change == "3":
                extract_image_from_video(input('\n[+] Введите путь к файлу видео: '))
            elif user_change == "4":
                clip_from_image(input('\n[+] Введите путь к папке с картинками: '), str(path_dir/(str(i) + '.mp4')),
                                input('[+] Введите продолжительность показа кадра (прим.: 0.1 или 1): '))
            elif user_change == "5":
                video_speed(input('\n[+] Введите имя видео: '), str(path_dir/(str(i) + '.mp4')),
                            input('\n[+] Введите коэффициент ускорения видео: '))
            elif user_change == "6":
                if i != 0:
                    shutil.move(str(path_dir/(str(i-1) + '.mp4')), input('[+] Введите название клипа: '))
            elif user_change == "7":
                if i != 0:
                    os.remove(str(path_dir/(str(i-1) + '.mp4')))
                    i -= 2
            elif user_change == "8":
                if i != 0:
                    shutil.move(str(path_dir/(str(i-1) + '.mp4')), input('[+] Введите название клипа: '))
                exit(0)
            else:
                print(RED + '\n[-] Неопознанный выбор. Повторите снова' + RESET)


if __name__ == "__main__":
    main()

