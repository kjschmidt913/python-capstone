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
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]

    

    template = loader.get_template('polls/index.html')
    context = {

        'Song': chooseSong()
    }
    return HttpResponse(template.render(context, request))
