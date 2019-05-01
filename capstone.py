import random

allData = {'Sweetener': {
    'raindrops (an angel cried)': ['When raindrops fell down from the sky',
                                   'The day you left me, an angel cried',
                                   'Oh, she cried, an angel cried',
                                   'She cried'],
    'blazed': ['There is something between us, I can see it right now',
               'Your magnetic demeanor, that\'s something can\'t be found',
               '(I thought that I was dreaming \'til my love came around)',
               '(Now I just come on over, show you how we get down)'
               'Shawty, you can get blazed',
               'I can\'t believe that you are here, I can\'t believe it\'s happening',
               'What are the odds that you\'d appear?',
               'The universe so vast to me',
               'Seven billion is on the Earth',
               'Could\'ve been anywhere, but you\'re here with me',
               'Should I play lotto? What\'s it worth?',
               'I must be on, so clear to me',
               'Once I have you, I will never let you, never let you,'
               'Once I have you, I will never let you, never let you go',
               'Never let you, never let you go',
               'Never let you, never let you go',
               'Never let you, never let you go',
               'Never let you',
               'There is something between us, I can see it right now',
               'Your magnetic demeanor, that\'s something can\'t be found',
               '(I thought that I was dreaming \'til my love came around)',
               '(Now I just come on over, show you how we get down)'
               'Shawty, you can get blazed',
               'Look at you, love, you are the same',
               'You have a light you cannot hide',
               'Yes, you may have a different face',
               'But your soul is the same inside',
               'I don\'t care who is listening',
               '\'Cause they be making fun of this on TV',
               'They wouldn\'t laugh if they were inside my past life',
               'With you and they were me',
               'Once I have you, I will never let you, never let you,'
               'Once I have you, I will never let you, never let you go',
               'Never let you, never let you go',
               'Never let you, never let you go',
               'Never let you, never let you go',
               'Never let you',
               'Don\'t think that it cannot happen, \'cause it can',
               'Shawty, you can get blazed',
               'Sleep if you want, and wake up in love again',
               'Shawty, you can get blazed',
               'Once I have you, I will never let you, never let you,'
               'Once I have you, I will never let you, never let you go',
               'Never let you, never let you go',
               'Never let you, never let you go',
               'Never let you, never let you go',
               'Never let you'
               ],
    'R.E.M.': ['Mhm, last night, boy, I met you, yeah',
               'When I was asleep (sleep)',
               'You\'re such a dream to me, mmm, woah',
               'And it was on a day like this, yeah',
               'If you can believe',
               'If you can believe (If you can believe)',
               'You\'re such a dream to me',

               'Before you speak, don\'t move',
               '\'Cause I don\'t wanna wake up',
               'Wake up, wake up, wake up',
               'Don\'t wanna wake up, oh',
               'Wake up, wake up, wake up',
               'Boy, you\'re such a dream if you can believe, ayy',
               'Boy, you\'re such a dream to me',

               'Excuse me, um, I love you',
               'I know that\'s not the way to start a conversation, trouble',
               'I watch them other girls when they come and bug you',
               'But I felt like I knew you, so I just wanted to hug you',
               'Plus, you don\'t know your way around',
               'You can stop your playing now',
               'All your worries, lay \'em down, shh, don\'t say it loud',
               'Is this real, baby?',
               '(Bum, bum, bum, bum, bum, bum, bum, bum, bum, bum, bum)',
               'You like?',
               'I love you',
               'Who starts a conversation like that? Nobody, but I do',
               'But you are not a picture, I can\'t cut you up and hide you',
               'I\'ll get you out my mind, mhm, I tried to',
               'But I just want to stand and yell',
               'I will never dare to tell',
               'Think I heard some wedding bells, shh, keep it to yourself',
               'Is this real? (Is this real?)',

               'Before you speak, don\'t move',
               '\'Cause I don\'t wanna wake up',
               'Wake up, wake up, wake up',
               'Don\'t wanna wake up, oh no',
               'Wake up, wake up, wake up',
               '\'Cause you\'re such a dream if you can believe',
               'You\'re such a dream to me, mmm, boy',

               'I could buy you anything, but I cannot buy you',
               'Before your boy gets smart, I would never try to',
               'You know I\'m thinking to myself, What happened, why you?',
               'But when I see you in my dreams, psh, I knew',
               'You know how to treat it, you know how to eat it',
               'You know how to beat it (I know how to keep it)',
               'The Good Housekeeping Seal',
               '(Bum, bum, bum, bum, bum, bum, bum, bum, bum, bum, bum)',
               'I don\'t just wanna touch you',
               'I\'m tryna turn two single people into a couple',
               'What\'s your next month like? Tell me what ya up to',
               'We can leave right now, boy, you don\'t need a duffle',
               'What about La Perla? Let Vickie keep her secret',
               'Boy, it ain\'t no secret if I know you\'re gonna peep it, oh',

               'Before you speak, don\'t move',
               '\'Cause I don\'t wanna wake up',
               'Wake up, wake up, wa-wake up',
               'Wake up, wake up, wake up, wa-wake up',
               'Oh, I don\'t wanna',

               '\'Cause you\'re such a dream (does this end?)',
               'If you can believe, you\'re such a dream to me',
               'To me, mmm, boy, to me'
               ]
    # 'God is a woman': 'lyrics here',
    # 'sweetener': 'lyrics here',
    # 'successful': 'lyrics here',
    # 'everytime': 'lyrics here',
    # 'breathin': 'lyrics here',
    # 'no tears left to cry': 'lyrics here',
    # 'borderline': 'lyrics here',
    # 'goodnight n go': 'lryics here',
    # 'pete davidson': 'lyrics here',
    # 'get well soon': 'lyrics here'
}, 'Thank U, Next': {
    'imagine': ['Step up the two of us, nobody knows us',
                'Get in the car like, "Skrrt"',
                'Staying up all night, order me pad thai',
                'Then we gon\' sleep \'til noon',
                'Me with no makeup, you in the bathtub',
                'Bubbles and bubbly, ooh',
                'This is a pleasure, feel like we never',
                'Act this regular',

                'Click, click, click and post',
                'Drip-drip-dripped in gold',
                'Quick, quick, quick, let\'s go',
                'Kiss me and take off your clothes',

                'Imagine a world like that',
                'Imagine a world like that',
                'We go like up \'til I\'m \'sleep on your chest',
                'Love how my face fits so good in your neck',
                'Why can\'t you imagine a world like that?',
                'Imagine a world',

                'Knew you were perfect, after the first kiss',
                'Took a deep breath like, "Hoo"',
                'Feels like forever, baby, I never',
                'Thought that it would be you',
                'Tell me your secrets, all of the creep shit',
                'That\'s how I know it\'s true',
                'Baby, direct it, name in the credits',
                'Like the movies do',

                'Click, click, click and post',
                'Drip-drip-dripped in gold',
                'Quick, quick, quick, let\'s go',
                'Kiss me and take off your clothes',

                'Imagine a world like that',
                'Imagine a world like that',
                'We go like up \'til I\'m \'sleep on your chest',
                'Love how my face fits so good in your neck',
                'Why can\'t you imagine a world like that?',
                'Imagine a world',

                'Can you imagine it?',
                'Can you imagine it?',
                'Can you imagine it?',
                'Can you imagine it?',
                'Can you imagine it? (Can you imagine?)',
                'Can you imagine it? (Can you imagine?)',
                'Can you imagine it? (Ooh)',
                'Imagine that',
                'Imagine it, imagine it',
                'Imagine it, imagine it',
                'Imagine, imagine',
                'Imagine, imagine',
                'Imagine, imagine'

                ],
    'needy': ['If you take too long to hit me back',
              'I can\'t promise you how I\'ll react',
              'But all I can say',
              'Is at least I\'ll wait for you',

              'Lately I\'ve been on a roller coaster',
              'Tryna get a hold of my emotions',
              'But all that I know',
              'Is I need you close',

              'And I\'ma scream and shout for what I love',
              'Passionate, but I don\'t give no fucks',
              'I admit that I\'m a lil\' messed up',
              'But I can hide it when I\'m all dressed up',

              'I\'m obsessive and I love too hard',
              'Good at overthinking with my heart',
              'How you even think it got this far?',
              'This far',

              'And I can be needy, way too damn needy',
              'I can be needy, tell me how good it feels to be needed',
              'I can be needy, so hard to please me',
              'I know it feels so good to be needed',

              'Sorry if I\'m up and down a lot (Yeah)',
              'Sorry that I think I\'m not enough',
              'And sorry if I say "sorry" way too much',

              'You can go ahead and call me selfish (Selfish)',
              'But after all this damage, I can\’t help it (Help it)',
              'But what you can trust is I need your touch',

              'I\'ma scream and shout for what I love',
              'Passionate, but I don\'t give no fucks',
              'I admit that I\'m a lil\' messed up',
              'But I can hide it when I\'m all dressed up',

              'I\'m obsessive and I love too hard',
              'Good at overthinking with my heart',
              'How you even think it got this far?',
              'This far',

              'And I can be needy, way too damn needy',
              'I can be needy, tell me how good it feels to be needed',
              'I can be needy, so hard to please me',
              'I know it feels so good to be needed',
              ],
    'NASA': ['This is one small step for woman',
             'One giant leap for woman-kind',

             'I\'d rather be alone tonight',
             'You can say "I love you" through the phone tonight',
             'Really don\'t wanna be in your arms tonight',
             'I\'ll just use my covers to stay warm tonight',
             'Think I\'m better off here all alone tonight',
             'Ain\'t no checkin\' on when I get home tonight',
             'Just makin\' sure I\'m good on my own tonight',
             'Even though there isn\'t nothin\' wrong tonight',

             'Yeah, I\'m just sayin\', baby',
             'I can\'t really miss you if I\'m with you',
             'And when I miss you, it\'ll change the way I kiss you',
             'Baby, you know time apart is beneficial',
             'It\'s like I\'m the universe and you\'ll be N-A-S-A',

             'Give you the whole world, I\'ma need space',
             'I\'ma need space, I\'ma, I\'ma need',
             'You know I\'m a star; space, I\'ma need space',
             'I\'ma need space, I\'ma, I\'ma need space (N-A-S-A)',
             'Give you the whole world, I\'ma need space',
             'I\'ma need space, I\'ma, I\'ma need',
             'You know I\'m a star; space, I\'ma need space',
             'I\'ma need space, I\'ma, I\'ma need space (N-A-S-A)',

             'Bottom line',
             'Usually, I would love it if you stayed the night',
             'I just think I\'m on another page tonight',
             'It ain\'t nothing wrong with saying I need me time',

             'Usually, I would orbit around you',
             'But gravity seems to be the only thing that\'s pulling me',
             'You\'ll be my rise and shine soon as them stars align, mmm',

             'Baby, I can\'t really miss you if I\'m with you',
             'And when I miss you, it\'ll change the way I kiss you',
             'Baby, you know time apart is beneficial',
             'It\'s like I\'m the universe and you\'ll be N-A-S-A',

             'Give you the whole world, I\'ma need space',
             'I\'ma need space, I\'ma, I\'ma need',
             'You know I\'m a star; space, I\'ma need space',
             'I\'ma need space, I\'ma, I\'ma need space (N-A-S-A)',
             'Give you the whole world, I\'ma need space',
             'I\'ma need space, I\'ma, I\'ma need',
             'You know I\'m a star; space, I\'ma need space',
             'I\'ma need space, I\'ma, I\'ma need space (N-A-S-A)',

             'You don\'t wanna leave me, but I\'m tryna self-discover',
             'Keep me in your orbit and you know you\'ll drag me under',
             'You don\'t wanna leave me, but I\'m tryna self-discover',
             '(You don\'t wanna leave me, but I\'m tryna self-discover)',
             'Keep me in your orbit and you know you\'ll drag me under',
             '(Keep me in your orbit and you know you\'ll drag me under)',

             'I\'d rather be alone tonight',
             'You can say "I love you" through the phone tonight'

             ],
    # 'bloodline': 'lyrics here',
    # 'fake smile': 'lyrics here',
    # 'bad idea': 'lyrics here',
    # 'make up': 'lyrics here',
    # 'ghostin': 'lyrics here',
    # 'in my head': 'lyrics here',
    # '7 rings': 'lyrics here',
    # 'thank u, next': 'lyrics here',
    # 'break up with your girlfriend, i\'m bored': 'lryics here'
}
}


def randomIndex(length):
    index = random.randint(1, length)
    return index


def chooseSong():
    albumPick = random.choice(list(allData.keys()))
    print(albumPick)
    songPick = random.choice(list(allData[albumPick].keys()))
    print(songPick)

    lyricIndex = randomIndex(len(allData[albumPick][songPick]) -1)

    lyric1 = allData[albumPick][songPick][lyricIndex]
    lyric2 = allData[albumPick][songPick][lyricIndex + 1]

    lyrics = allData[albumPick][songPick][lyricIndex] + '\n' + allData[albumPick][songPick][lyricIndex + 1]

    print(lyrics)


chooseSong()
