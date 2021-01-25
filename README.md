# videobase

## videodownload 
функция, получает на вход файл youtube.csv, в котором находятся ссылки на видео в youtube. видео скачивается в папку с программой
 и в ту же папку сохраняет .csv файл с информацией обо всех видео (название, fps, объём в Mb, разрешение, url)
 На вход принимает имя файла.csv в котором хранится список видео для загрузки
```videodownload('youtube.csv')```
Поддерживаются различные настройки разрешения, формата.
```
yt.streams
  ... .filter(progressive=True, file_extension='mp4')
  ... .order_by('resolution')
  ... .desc()
  ... .first()
  ... .download()
 ```
 Есть возможность отсортировать по качеству и выбрать лучшее разрешение
 ```
 yt.streams.filter(progressive=True).order_by('resolution').desc().all()
  [<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">,
  <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">]```
  ```
  
 ***
 
## videoframe
Функция, которая по файлу видео создаёт папку с кадрами из этого видео с определённой частотой
На вход принимает 2 аргумента: имя файла и количество кадров в секунду(fps)
```videoframe('anything.mp4', 2)```
Для названия папки берется имя видеофайла, предварительно удаляются все знаки препинания и другой "муссор", также применяется транслитерация, чтобы избежать проблем с записью на разных системах.
