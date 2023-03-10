import keys
import tweepy

if __name__ == "__main__":

    oauth1_user_handler = tweepy.OAuth1UserHandler(
        keys.api_key, keys.api_secret,
        callback="oob"
    )

    # printing url
    print(oauth1_user_handler.get_authorization_url())

    # ادخل الرابط المطبوع وسجل بحسابك الي تبي يصير بوت قرآن وبعدها ادخل الرمز
    # enter the printed url and sign with the account you want to make quran bot then enter PIN

    PIN = input("Please enter PIN code from twitter website: ")
    access_token, access_token_secret = oauth1_user_handler.get_access_token(PIN)

    print('access_token = "%s"' % oauth1_user_handler.access_token)
    print('access_token_secret = "%s"' % oauth1_user_handler.access_token_secret)
