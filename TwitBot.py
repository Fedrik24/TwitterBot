import tweepy
import logging
import os

logger = logging.getLogger()

def Api_FedrikBot():
    auth = tweepy.OAuthHandler("API KEY", "API SECRET")
    auth.set_access_token("ACCTOKEN", "ACCSECRET")
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api