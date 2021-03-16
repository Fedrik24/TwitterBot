import tweepy
import logging
import os

logger = logging.getLogger()

def Api_FedrikBot():
    auth = tweepy.OAuthHandler("dqnCuqjawW9X8XM6RIq3oRdFX", "8ePSGcxt0IPJRGztrpnlkavlP8W0COaa8FiUyYMk7AEnl9Hc9F")
    auth.set_access_token("1301733212167659521-LVPO2IH91hQzvul50GogQiQSfwumqo", "6QtrdZkfz4Nt6rRmgSGI7TZ7nkUvNgB4eD0ItXG1fjv8e")
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api