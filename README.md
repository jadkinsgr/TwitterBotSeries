# Twitter Bot ReadMe

ReadMe Documentation for how to get up and running with a Twitter bot on the Twitter API!

## Developer Access

THE FIRST STEP IS TO APPLY FOR DEVELOPER ACCESS ON TWITTER.

Head on out to https://developer.twitter.com/en/apply-for-access, here you will be able to get started. The process is a bit long, however, if you have a good idea of what you would like to do you should have all you need to get started. Your application does go to a real person before it is approved so make sure to familiarize yourself with Twitter's rules and regulations on Twitter developer access and automation rules.

Automation rules
https://help.twitter.com/en/rules-and-policies/twitter-automation

Rate Limits and developer agreements:
https://developer.twitter.com/en/developer-terms/agreement-and-policy


## Create your Config.py File
By this step, you should have your developer access granted, if so great! Nice Job!

Lets start with the first few steps we need to get started and that's by installing the module you will need for this step: Tweepy and integrating your API and Access keys (code displayed at the bottom)
In your terminal, run the command pip install tweepy to load that module onto your system. Want to learn more about the variety of modules? Learn more at https://pypi.org/.


1. In your terminal, run the command pip install tweepy to load that module onto your system. Want to learn more about the variety of modules? Learn more at https://pypi.org/.

2. Next up - we need to add those API and access keys. You can of course hard code yours in your script but that's not nearly as helpful or safe if you need to share your code or better yet, post it somewhere! So let's add it to your system's environmental variables and use the OS module to call them.

3. I'm typically a Mac user (queue comments - but just know, I have windows OS on my machine too, I just prefer iOS). Anyways! There are a few ways to add objects to your machine's environment variables.

On macs, what used to be bash is now zshell on newer software versions that said in terminal
1. type "atom ~/.zshrc", hit enter - you're now in your environment variable screen - at the very top 
before everything just copy and paste the following code, replacing your variables:
export CONSUMER_KEY=“1234…”
export CONSUMER_SECRET=“1234…”
export ACCESS_TOKEN=“1234…”
export ACCESS_TOKEN_SECRET=“1234…”

Save, exit, reboot your code editor

if you have an error here - it's possible you do not have the ATOM text editor installed, if not, no big deal, replace atom with nano in step 1. Everyone should have Nano.

## Code base
```python
#environmentvariabletest.py
import os

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_secret)
```


```python
# config.py
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
