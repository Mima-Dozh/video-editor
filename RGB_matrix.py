from colorama import init, Fore
import os.path
from moviepy.editor import *
import time
import numpy as np
from PIL import Image

init()
RED = Fore.RED
RESET = Fore.RESET

def make_matr(arr, index, color):
    matr = color + '\n'
    for i in arr:
        for j in i:
            matr += str(j[index]).rjust(3) + ' '
        matr += '\n'
    return matr

def write_file(arr, path_to):
    with open(path_to, 'w') as file_to:
        red_matr = make_matr(arr, 0, 'RED')
        green_matr = make_matr(arr, 1, 'GREEN')
        blue_matr = make_matr(arr, 2, 'BLUE')
        file_to.write(red_matr + '\n\n'
                    + green_matr + '\n\n'
                    + blue_matr)

def time_parserr(time, duration):
    try:
        t = [int(i) for i in time.split(':')]
    except:
        print(RED + 'Не верный формат даты' + RESET)
        exit(1)
    
    size = len(t)
    if size > 3 or size == 0:
        print(RED + 'Не верный формат даты' + RESET)
        exit(1)
    if t[-1] > 59 or size > 1 and t[-2] > 59:
        print(RED + 'Не верный формат даты' + RESET)
        exit(1)
    s = 0
    for i in t:
        s *= 60
        s += i
    if duration < s:
        print(RED + 'Укажите время в пределах видео' + RESET)
        exit(1)
    return s

def find_RGB_matrix(path_from, path_to, time):
    clip  = VideoFileClip(path_from)
    frame = clip.get_frame(time_parserr(time), clip.duration)
    arr = np.array(frame)
    write_file(arr, path_to)
