
if __name__ == '__main__':
    print('Ура!')
    print('Исследование распространённости языков.')

    # the part of english speakers
    print(1121 / 7539)

    # the quantity of people learned Japanese
    print((128.3 - 128.2) / 128.3)

    english = 378.2
    russian = 153.9
    german = 76.0
    chinese = 908.7
    top3_total = english + russian + german
    print(chinese - top3_total)

    japanese_websites = 0.045
    chinese_websites = 0.043
    print(chinese_websites / japanese_websites)

    print(type(english))

    russian_web_part = 0.061
    web_popular = 10000000

    russian_web_popular = russian_web_part * web_popular
    print(russian_web_popular)
    print(type(russian_web_popular))

    russian_web_part2 = int(russian_web_part)
    web_popular2 = float(web_popular)

    print(russian_web_part2)
    print(web_popular2)


    total_web = 10
    total_speakers = 7539

    chinese_speakers = 1107
    chinese_web_part = 0.017

    english_speakers = 1121
    english_web_part = 0.539

    russian_speakers = 264.3
    russian_web_part = 0.061

    chinese_speakers_part = chinese_speakers / total_speakers
    print('Доля людей, говорящих на китайском:' , chinese_speakers_part)

    english_speakers_part = english_speakers / total_speakers
    print('Доля людей, говорящих на английском:' , english_speakers_part)

    russian_speakers_part = russian_speakers / total_speakers
    print('Доля людей, говорящих на русском:' , russian_speakers_part)