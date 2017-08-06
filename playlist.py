from __future__ import unicode_literals
import youtube_dl
import os
opts = {
    'format': 'bestaudio/best',
    'extractaudio':True,
    'audioformat':'mp3',
    'outtmpl': u'%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(opts) as ydl:
    #result = ydl.extract_info('https://www.youtube.com/playlist?list=PLZ7UWQadkaDPrv8oFjcc86JoSlaWFAFM7', download = False)
    ydl.download(['https://www.youtube.com/playlist?list=PLZ7UWQadkaDPrv8oFjcc86JoSlaWFAFM7'])

#os.system("youtube-dl -citk --buffer-size 144 FORMAT <https://www.youtube.com/playlist?list=PLZ7UWQadkaDPrv8oFjcc86JoSlaWFAFM7>")
