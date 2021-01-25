

import cv2
from pytube import YouTube
import pandas as pd
import re
import sys
import glob
import os


def transliterate(name):
    # Слоаврь с заменами
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
              'ю': 'u', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO',
              'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
              'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
              'Ю': 'U', 'Я': 'YA', ',': '', '?': '', ' ': '_', '~': '', '!': '', '@': '', '#': '',
              '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '=': '', '+': '',
              ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
              '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
              'Є': 'e', '—': ''}

    # Циклически заменяем все буквы в строке
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name


def videoframe(video, frame_fps):
    #video = '«Умная дорога» и беспилотники как ЦКАД обеспечит комфортную жизнь людям.mp4'

    # Создание папки
    folder_name = transliterate(video[:-4])
    folder_name = re.sub(r'[^\s\w]', '', folder_name)

    os.mkdir(folder_name)

    vidcap = cv2.VideoCapture(video)
    success, image = vidcap.read()
    # Изначальное количество fps указанное вручную
    video_fps = 30
    # Либо полученное из файла youtubeout.csv
    # df_out_in = pd.read_csv('youtubeout.csv')
    # video_fps = df_out_in.fps[(df_out_in['name'] == video)]
    # print(video_fps)

    # Указать необходимый FPS для дробления видео на кадры
    #frame_fps = 1

    fps_coefficient = video_fps / frame_fps

    count = 0
    frame = 0
    success = True
    while success:
        if frame % fps_coefficient == 0:
            cv2.imwrite(folder_name + "/frame%d.jpg" % count, image)
            # cv2.imwrite("«Умная дорога» и беспилотники как ЦКАД обеспечит комфортную жизнь людям/frame%d.jpg" % count, image)
            # cv2.imwrite("fr/frame%d.jpg" % count, image)   # save frame as JPEG file
            # cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
            count += 1
        success, image = vidcap.read()
        frame += 1

    vidcap.release()
    cv2.destroyAllWindows()



videoframe('«Умная дорога» и беспилотники как ЦКАД обеспечит комфортную жизнь людям.mp4', 1)
