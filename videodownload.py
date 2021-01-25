from pytube import YouTube
import pandas as pd
import re
import sys
import glob
import os

BYTE_TO_MEGABYTE_COEFFICIET = 1048576  # 1024 * 1024

def videodownload(youtube):
    # Чтение файла со списком видео
    df = pd.read_csv(youtube)

    df_out = pd.DataFrame(columns=['name', 'fps', 'weight_mb', 'resolution', 'url'])

    for i in range(df.shape[0]):
        # Инициализируем экземляр YouTube
        yt = YouTube(df.url[i])

        # Выбираем файл для загрузки
        stream = yt.streams.first()

        # Получаем fps
        fps = stream.fps
        # Парсим строку, чтобы узнать разрешение видео
        # stream_str = str(stream)
        # re.findall(r"res=..+?\"", stream_str)[0][5:-1]
        res = stream.resolution
        # Загружаем видео
        video = yt.streams.first().download()
        # Находим последний загруженный файл и узнаем его имя
        list_of_files = glob.glob('*.mp4')  # после * укажите нужный формат видео
        latest_file = max(list_of_files, key=os.path.getctime)
        # Считываем вес файла
        statinfo = os.stat(latest_file)
        # Узнаем вес в байтах, Переводим в MB
        weight_mb = statinfo.st_size / BYTE_TO_MEGABYTE_COEFFICIET
        # print(statinfo.st_size, "байт")
        # print(weightmb, "мегабайт")
        row = ['name', 'fps', 'weight_mb', 'resolution', 'url']
        df_out_to = pd.DataFrame([[latest_file, fps, weight_mb, res, df.url[i]]], columns=row)
        df_out = df_out.append(df_out_to, ignore_index=True)

    # Записываем информацию о видео в csv
    df_out.to_csv('youtubeout.csv')

    # Проверяем
    df_out_in = pd.read_csv('youtubeout.csv')


videodownload('youtube.csv')