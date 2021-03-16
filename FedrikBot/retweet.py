import tweepy
import logging
from TwitBot import Api_FedrikBot
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
           
            return
        if not tweet.favorited:
            
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=False)
        if not tweet.retweeted:
            
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=False)

    def on_error(self, status):
        logger.error(status)

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

def ReTweet(keywords):
    api = Api_FedrikBot()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
   ReTweet(["#OLLIcin", 
          "#Kureiji_Ollie",
          "#Anya_Melfissa",
          "#POGVOLIA",
          "#iomemes",
          "#Moona_Hoshinova",
          "#Risu_meme",
          "#Hololive",
          "#hololive",
          "#Holostar",
          "#holostar",
          "#callillust",
          "#TAKAMORI",
          "#inART",
          "#gawrt",
          "#ameliaRT",
          "#いなート",
          "#teamates",
          "#kfpmemes",
          "#ココここ",
          "#holoJPmeme",
          "#天音かなたボイス",
          "#ふぁんでっど",
          "#ぺこらーと",
          "#絵かゆ",
          "猫又おかゆ",
          "#コレクシオン",
          "#百鬼絵巻",
          "#祭絵 ",
          "natsuiromatsuri",
          "#スケベなアロ絵",
          "#アロ絵",
          "#さくらみこ",
          "#miko_Art",
          "Sakura Miko",
          "#soraArt",
          "tokino_sora",
          "shishirobotan",
          "#ししらーと",
          "holostarstv",
          "astelleda",
          "#つのまきあーと ",
          "#ドドドライブ",
          "#しょこらーと",
          "#らみらいぶ ",
          "#ポルカおるか"])