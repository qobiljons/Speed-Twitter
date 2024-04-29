from measure_speed_and_tweet import InternetSpeedTwitterBot
import os

username = os.environ["username"]
password = os.environ["password"]


speed_twitter = InternetSpeedTwitterBot()

speed = speed_twitter.get_internet_speed()

tweet = speed_twitter.tweet(username=username, password=password, speed=speed)