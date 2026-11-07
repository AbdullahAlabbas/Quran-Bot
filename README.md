# Quran-Bot

A Twitter bot that tweets a random verse from the Quran every six hours. It ran as [@QuranBotAR](https://twitter.com/QuranBotAR).

> **Archived:** this project is no longer maintained. It uses the Twitter API v1.1 `update_status` endpoint, which X no longer offers on its free tier, so it is kept here for reference.

![Example tweet](https://user-images.githubusercontent.com/106891021/207991291-11e78394-125c-4f08-bd93-d6c9e361fa52.png)

## How it works

- `Quran.json` holds the full Arabic text of the Quran (in the AlQuran Cloud API format).
- `Quran/Quran.py` picks a random surah and ayah from it.
- `Quran/tweet.py` skips any verse longer than 280 characters, tweets one, then sleeps for six hours and repeats.
- `Quran/create_keys.py` walks you through Twitter's PIN-based OAuth flow to get an access token for the bot account.

## Running it

Requires Python 3 and [Tweepy](https://www.tweepy.org/).

```bash
pip install tweepy
```

1. Put your app's `api_key` and `api_secret` in `keys.py`. The `bearer_token` is not needed.
2. If you don't have an access token for the bot account yet, run `python -m Quran.create_keys`, open the printed link, sign in with the bot account, enter the PIN, and copy the printed tokens into `keys.py`.
3. Start the bot from the repo root:

```bash
python -m Quran.tweet
```

Never commit `keys.py` with real keys in it.

## Credits

Thanks to [@Wouze](https://github.com/Wouze) for adding the key-creation script.

## License

[MIT](LICENSE)
