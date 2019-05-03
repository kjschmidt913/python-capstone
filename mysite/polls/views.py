import random

from django.http import HttpResponse
from django.template import loader

from .models import Songs


def randomIndex(length):
    index = random.randint(0, length)
    return index


def index(request):
    template = loader.get_template('polls/index.html')

    albumPick = random.choice(list(Songs.allData.keys()))
    songPick = random.choice(list(Songs.allData[albumPick].keys()))

    lyricIndex = randomIndex(len(Songs.allData[albumPick][songPick]) - 2)
    context = {
        'Lyric_One': Songs.allData[albumPick][songPick][lyricIndex] ,
        'Lyric_Two' : Songs.allData[albumPick][songPick][lyricIndex + 1],
        'Album' : albumPick,
        'Song' : songPick

    }
    return HttpResponse(template.render(context, request))
