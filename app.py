from __future__ import unicode_literals
import youtube_dl
from youtube_search import YoutubeSearch

song_done = ["당신은 사랑받기 위해 태어난 사람",
            "구주의 십자가 보혈로",
            "주의 음성을 내가 들으니",
            "내 주를 가까이 하려함은",
            "십자가를 질수 있나",
            "예수 나를 위하여 십자가를 질때",
            "예수 나를 오라하네",
            "죄에서 자유를 얻게함은",
            "곤한 내 영혼 편히 쉴곳과",
            "불길 같은 주성령",
            "변찮은 주님의 사랑과",
            "나의 죄를 씻기는",
            "주 나의 모든것",
            "내 영혼아 여호와를 송축하라",
            "나의 아버지",
            "그는 여호와 창조의 하나님",
            "하나님 우리와 함께 하시모니",
            "우리 주의 성령이 내게 임하여",
            "내 눈 주의 영광을 보네",
            "예수 결박 푸셨도다",
            "주님 큰 영광 받으소서",
            ]

song_list = [
            "모든 영광을 하나님께",
            "주님과 함께 하는 이 고요한 시간"]

print(len(song_list))

for i in song_list:
    result = YoutubeSearch(i, max_results=1).to_dict()
    print(i + ": " + result[0]['url_suffix'])

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(["https://youtube.com/" + result[0]['url_suffix']])

