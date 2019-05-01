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
}, 'Thank U, Next': 'hi'
}

albums = ['Sweetener', 'Thank U, Next']



def randomIndex(length):
    index = random.randint(1, length)
    print(index)

randomIndex(400)

def chooseSong():
    lyric = allData['Sweetener']['blazed']
    print(lyric)

chooseSong()

