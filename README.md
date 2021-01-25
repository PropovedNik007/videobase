# videobase

## videodownload 
функция, получает на вход файл youtube.csv, в котором находятся ссылки на видео в youtube. видео скачивается в папку с программой
 и в ту же папку сохраняет .csv файл с информацией обо всех видео (название, fps, объём в Mb, разрешение, url)
 На вход принимает имя файла.csv в котором хранится список видео для загрузки
```videodownload('youtube.csv')```
 
 ***
 
## videodownload 
Функция, которая по файлу видео создаёт папку с кадрами из этого видео с определённой частотой
На вход принимает 2 аргумента: имя файла и количество кадров в секунду(fps)
```videoframe('anything.mp4', 2)```
