import json
from random import randrange


def main():
    randomVerse()


def randomVerse():
    
    with open("Quran.json") as QURAN:
        quranJSON = json.load(QURAN)

    surah = randrange(114)
    verse = randrange(286)

    try:
        verse = quranJSON["data"]["surahs"][surah]["ayahs"][verse]["text"]
        return verse

    except IndexError:
        main()

if __name__ == "__main__":
    main()