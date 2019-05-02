import random

from django.http import HttpResponse
from django.template import loader

from .models import Songs


def randomIndex(length):
    index = random.randint(0, length)
    return index

def chooseSong():
    albumPick = random.choice(list(Songs.allData.keys()))
    songPick = random.choice(list(Songs.allData[albumPick].keys()))

    lyricIndex = randomIndex(len(Songs.allData[albumPick][songPick]) - 2)

    lyrics = Songs.allData[albumPick][songPick][lyricIndex] + \
        '\n' + Songs.allData[albumPick][songPick][lyricIndex + 1]

    return lyrics


def index(request):
    template = loader.get_template('polls/index.html')

    albumPick = random.choice(list(Songs.allData.keys()))
    songPick = random.choice(list(Songs.allData[albumPick].keys()))

    lyricIndex = randomIndex(len(Songs.allData[albumPick][songPick]) - 2)
    context = {
        'Song': chooseSong(),
        'Lyric_One': Songs.allData[albumPick][songPick][lyricIndex] ,
        'Lyric_Two' : Songs.allData[albumPick][songPick][lyricIndex + 1]
    }
    return HttpResponse(template.render(context, request))
