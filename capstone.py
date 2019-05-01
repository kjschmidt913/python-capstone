import random

allData = {'Sweetener': {
    'raindrops (an angel cried)': ['lyrics here', 'and here'],
    'blazed': 'lyrics here',
    'the light is coming': 'lyrics here',
    'R.E.M.': 'lyrics here',
    'God is a woman': 'lyrics here',
    'sweetener': 'lyrics here',
    'successful': 'lyrics here',
    'everytime': 'lyrics here',
    'breathin': 'lyrics here',
    'no tears left to cry': 'lyrics here',
    'borderline': 'lyrics here',
    'goodnight n go': 'lryics here',
    'pete davidson': 'lyrics here',
    'get well soon': 'lyrics here'
}, 'Thank U, Next': {
    'imagine': ['lyrics here', 'and here'],
    'needy': 'lyrics here',
    'NASA': 'lyrics here',
    'bloodline': 'lyrics here',
    'fake smile': 'lyrics here',
    'bad idea': 'lyrics here',
    'make up': 'lyrics here',
    'ghostin': 'lyrics here',
    'in my head': 'lyrics here',
    '7 rings': 'lyrics here',
    'thank u, next': 'lyrics here',
    'break up with your girlfriend, i\'m bored': 'lryics here'
}
}


def randomIndex(length):
    index = random.randint(1, length)
    print(index)


randomIndex(400)


def chooseSong():
    albumPick = random.choice(list(allData.keys()))
    print(albumPick)
    songPick = random.choice(list(allData[albumPick].keys()))
    print(songPick)

chooseSong()
