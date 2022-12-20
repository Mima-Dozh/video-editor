import argparse
from colorama import init, Fore
from merge_videos import merge_videos
from clip_video import clip_video
from extract_image_from_video import extract_image_from_video
from video_speed import video_speed
from clip_from_image import clip_from_image

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED


def main():
    while True:
        user_change = input(RESET + '\n[+] Выберите действие:\n   [1] Объединить видео\n   [2] Вырезать фрагмент\n   '
                            '[3] Извлечь кадры из видео\n   [4] Создать клип из картинок\n   '
                            '[5] Изменить скорость видео\n   [6] Выход\n   >>> ')
        if user_change == "1":
            merge_videos(input('\n[+] Введите путь к папке с файлами: '),
                         input('[+] Введите название для объединенного видео: '))
        elif user_change == "2":
            clip_video(input('\n[+] Введите путь к файлу видео: '), input('[+] Введите время начала фрагмента\n'
                                                                          '   - пример: 02:25\n   >>> '),
                       input('[+] Введите время окончания фрагмента\n'
                             '   - пример: 03:50\n   >>> '))
        elif user_change == "3":
            extract_image_from_video(input('\n[+] Введите путь к файлу видео: '))
        elif user_change == "4":
            clip_from_image(input('\n[+] Введите путь к папке с картинками: '), input('[+] Введите название клипа: '),
                            input('[+] Введите продолжительность показа кадра (прим.: 0.1 или 1): '))
        elif user_change == "5":
            video_speed(input('\n[+] Введите имя видео: '), input('\n[+] Введите название для нового видео: '),
                        input('\n[+] Введите коэффициент ускорения видео: '))
        elif user_change == "6":
            exit(0)
        else:
            print(RED + '\n[-] Неопознанный выбор. Повторите снова' + RESET)


if __name__ == "__main__":
    main()

