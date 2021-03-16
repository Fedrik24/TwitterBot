from retweet import ReTweet
import time 

class Start:
    def __init__(self):
        print("\nStarting to Retweet")
        time.sleep(3)
        self.Ret()
    def Ret(self):
        Tweet_list = ["OLLIcin", 
                      "Kureiji_Ollie",
                      "Anya_Melfissa",
                      "POGVOLIA",
                      "iomemes",
                      "Moona_Hoshinova",
                      "Risu_meme","Hololive",
                      "hololive",
                      "Holostar",
                      "holostar"]
        ReTweet(Tweet_list)
       


if __name__ == "__main__":
    s = Start()
    s