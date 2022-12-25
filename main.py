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
from retry import retry
import uuid

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED

def save_video(a):
    if len(a) == 0:
        print(RED + "Здесь нечего сохранять" + RESET)
        return
    
    i = 0
    while True:
        try:
            shutil.move((str(a[0])), input('[+] Введите название клипа: ') + '.' + str(a[0]).split('.')[1])
        except:
            if i > 10:
                print(RED + "Я устал ошибаться" + RESET)
                return
            print(RED + "Попробуй другое расширение фаила\n" + RESET)
            i += 1
            continue
        break

def create_file_name(path, index, rr):
    return str(path / (str(uuid.uuid4()) + f'_{index}' + rr))


def main():
    with tempfile.TemporaryDirectory(dir = Path()) as tmpdirname:
        i = 0
        j = 0
        path_dir = Path(tmpdirname)
        while True:
            try:
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
                    clip_from_image(input('\n[+] Введите путь к папке с картинками: '), create_file_name(path_dir, i, '.mp4'),
                                    input('[+] Введите продолжительность показа кадра (прим.: 0.1 или 1): '))
                elif user_change == "5":
                    video_speed(input('\n[+] Введите имя видео: '), create_file_name(path_dir, i, '.mp4'),
                                input('\n[+] Введите коэффициент ускорения видео: '))
                elif user_change == "6":
                    save_video(list(path_dir.glob(f'*_{str(i-1)}.*')))
                    i-=1
                elif user_change == "7":
                    if i != 0:
                        os.remove(str(path_dir/(str(i-1) + '.mp4')))
                        i -= 2
                elif user_change == "8":
                    save_video(list(path_dir.glob(f'*_{str(i-1)}.*')))
                    return
                else:
                    print(RED + '\n[-] Неопознанный выбор. Повторите снова' + RESET)
            except:
                if j > 10:
                    print(RED + "Я устал ошибаться")
                    exit(0)
                j+=1
                print(RED + '\nЧерти мешают работе!\n Попробуйте еще раз' + RESET)

if __name__ == "__main__":
    main()

