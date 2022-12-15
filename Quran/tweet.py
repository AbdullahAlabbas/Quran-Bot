import tweepy
import keys
from Quran.Quran import randomVerse
import time 


def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)



def tweet(api: tweepy.API, message: str):

    api.update_status(message)

    print('Tweeted successfully!')
    
    
if __name__ == '__main__':
    
    api = api()
    while True:
        verse = randomVerse()
        while verse == None or len(verse) > 280:
            verse = randomVerse()
        
        tweet(api, verse)
        time.sleep(21600)
