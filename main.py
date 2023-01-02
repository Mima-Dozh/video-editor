import argparse
import os
from colorama import init, Fore
from merge_videos import merge_videos
from clip_video import clip_video
from extract_image_from_video import extract_image_from_video
from video_speed import video_speed
from fadein_video import fadein_video
from fadeout_video import fadeout_video
from rotate_video import rotate_video
from clip_from_image import clip_from_image
import tempfile
from pathlib import Path
import shutil
import uuid

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED
YELLOW = Fore.YELLOW


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

def check_path(input_text):
    p = input(input_text)
    i = 0
    while not os.path.exists(p):
        if i > 10:
            print(RED + "Я устал искать фаилы, дальше ты сам!" )
            print_mem()
        print(RED + "Я не знаю таких фаилов. Может ты перепутал?\n Попробуй другое имя или путь")
        p = input(RESET + input_text)
        i += 1
    return p

def print_mem():
    print('        ⢀⣤⣤⣶⠶⠶⣶⣤⣤⡀\n'+
        '⠀⠀⠀⠀⠀⢀⣴⠾⠛⠉⠀⢠⣾⣴⡾⠛⠻⣷⣄\n'+
        '⠀⠀⢶⣶⣶⣿⣁⠀⠀⠀⠀⢸⣿⠏⢀⣤⣶⣌⠻⣦⡀⠀⠀⠀\n'+
        '⠀⠀⣴⡟⠁⢉⣙⣿⣦⡀⠀⢸⡏⣴⠟⢡⣶⣿⣧⡹⣷⡀⠀⠀\n'+
        '⠀⣼⠏⢀⣾⠟⠛⠛⠻⣿⡆⠀⠀⢿⣄⠀⠙⠉⠹⣷⡸⣷⠀⠀\n'+
        '⢠⣿⠀⢸⡿⢿⠇⠀⠀⣾⠇⠀⣀⣈⠻⢷⣤⣤⣤⡾⠃⢹⣇⠀\n'+
        '⢸⣿⠀⢸⣧⣀⣀⣠⣾⢋⣴⢿⣿⡛⠻⣶⣤⣉⠁⠀⠀⠀⣿⠀\n'+
        '⠈⣿⠀⠀⠙⠛⠛⠋⠁⣼⣯⣀⣿⠿⠶⠟⠉⠛⢷⣄⠀⠀⣿⡇\n'+
        '⠀⣿⠀⠀⠀⠀⠀⠀⠀⣿⡏⠉⠁⠀⠀⢀⣴⢶⣄⢻⡇⠀⢸⡇\n'+
        '⠀⢻⣇⠀⠀⠀⠀⠀⢠⡿⢀⣀⢠⣾⠷⣾⣧⡶⠿⠟⠁⠀⣾⡇\n'+
        '⠀⠈⣿⣧⡀⠀⠀⣠⣿⣷⠟⢻⣿⣷⡾⠛⠉⠀⠀⠀⠀⢀⣿⠀\n'+
        '⠀⠀⢹⣿⢻⣦⡀⠉⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀\n'+
        '⠀⠀⠀⠛⠀⠈⠻⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠟⠀⠀\n')

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
                                    '[5] Изменить скорость видео\n\t[6] Эффект fade-in\n\t[7] Эффект fade-out\n\t'
                                    '[8] Изменить угол картинки\n\t[9] Сохранить изменения\n\t[10] Отменить изменения\n\t'
                                    '[11] Посмотреть результат\n\t[12] Выход\n>>> ')
                if user_change == "1":
                    merge_videos(check_path('\n[+] Введите путь к папке с файлами: '),
                                    create_file_name(path_dir, i, '.mp4'))
                elif user_change == "2":
                    clip_video(check_path('\n[+] Введите путь к файлу видео: '), input('[+] Введите время начала фрагмента\n'
                                                                                    '   - пример: 02:25\n   >>> '),
                                input('[+] Введите время окончания фрагмента\n'
                                        '   - пример: 03:50\n   >>> '))
                elif user_change == "3":
                    extract_image_from_video(check_path('\n[+] Введите путь к файлу видео: '))
                elif user_change == "4":
                    clip_from_image(check_path('\n[+] Введите путь к папке с картинками: '), create_file_name(path_dir, i, '.mp4'),
                                    input('[+] Введите продолжительность показа кадра (прим.: 0.1 или 1): '))
                elif user_change == "5":
                    video_speed(check_path('\n[+] Введите имя видео: '), create_file_name(path_dir, i, '.mp4'),
                                input('\n[+] Введите коэффициент ускорения видео: '))
                elif user_change == "6":
                    fadein_video(check_path('\n[+] Введите путь к файлу видео: '), create_file_name(path_dir, i, '.mp4'),
                                 int(input('\n[+] Введите время эффекта: ')))
                elif user_change == "7":
                    fadeout_video(check_path('\n[+] Введите путь к файлу видео: '), create_file_name(path_dir, i, '.mp4'),
                                  int(input('\n[+] Введите время эффекта: ')))
                elif user_change == "8":
                    rotate_video(check_path('\n[+] Введите путь к файлу видео: '), create_file_name(path_dir, i, '.mp4'),
                                  int(input('\n[+] Введите угол поворота: ')))
                elif user_change == "9":
                    save_video(list(path_dir.glob(f'*_{str(i-1)}.*')))
                    i-=1
                elif user_change == "10":
                    i -=1
                    if i != 0:
                        os.remove(list(path_dir.glob(f'*_{str(i)}.*'))[0])
                        i -= 1
                elif user_change == "11":
                    i -=1
                    if i != 0:
                        os.startfile(list(path_dir.glob(f'*_{str(i)}.*'))[0])
                elif user_change == "12":
                    while i > 1:
                        a = input(YELLOW + 'Увас есть не сохраненый прогресс желаете его сохранить?\n(Да/Нет)')
                        if a.lower() == 'да':
                            save_video(list(path_dir.glob(f'*_{str(i-1)}.*')))
                            i-=1
                        elif a.lower() == 'нет':
                            break
                        else:
                            print(RED + "Ты наверно не понял у тебя только 2 варианта ответа\nДавай попробуем заного\n")
                    print(GREEN + 'Работа завершена\nОбращайтесь ещё!')
                    return
                else:
                    print(RED + '\n[-] Неопознанный выбор. Повторите снова' + RESET)
            except:
                if j > 10:
                    print(RED + "\nЯ устал ошибаться")
                    print_mem()
                    exit(0)
                j+=1
                print(RED + '\nЧерти мешают работе!\nПопробуйте еще раз' + RESET)


if __name__ == "__main__":
    main()

