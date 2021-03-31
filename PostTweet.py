# followfollowers.py
import tweepy
import logging
from config import create_api
import time
from datetime import datetime
import random
import os
from pyowm import OWM

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

api = create_api()


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'The best thing about a boolean is even if you are wrong, you are only off by a bit. (Anonymous)'
    elif answerNumber == 2:
        return 'Without requirements or design, programming is the art of adding bugs to an empty text file. (Louis Srygley)'
    elif answerNumber == 3:
        return 'Before software can be reusable it first has to be usable. (Ralph Johnson)'
    elif answerNumber == 4:
        return 'The best method for accelerating a computer is the one that boosts it by 9.8 m/s2. (Anonymous)'
    elif answerNumber == 5:
        return 'I think Microsoft named .Net so it wouldn’t show up in a Unix directory listing. (Oktal)'
    elif answerNumber == 6:
        return 'If builders built buildings the way programmers wrote programs, then the first woodpecker that came along would destroy civilization. (Gerald Weinberg)'
    elif answerNumber == 7:
        return 'There are two ways to write error-free programs; only the third one works. (Alan J. Perlis)'
    elif answerNumber == 8:
        return 'Ready, fire, aim: the fast approach to software development. Ready, aim, aim, aim, aim: the slow approach to software development. (Anonymous)'
    elif answerNumber == 9:
        return 'It’s not a bug – it’s an undocumented feature. (Anonymous)'
    elif answerNumber == 10:
        return 'One man’s crappy software is another man’s full-time job. (Jessica Gaston)'
    elif answerNumber == 11:
        return 'A good programmer is someone who always looks both ways before crossing a one-way street. (Doug Linder)'
    elif answerNumber == 12:
        return 'It’s not a bug – it’s an undocumented feature. (Anonymous)'
    elif answerNumber == 13:
        return 'It’s not a bug – it’s an undocumented feature. (Anonymous)'
    elif answerNumber == 14:
        return 'I think Microsoft named .Net so it wouldn’t show up in a Unix directory listing. (Oktal)'
    elif answerNumber == 15:
        return 'If builders built buildings the way programmers wrote programs, then the first woodpecker that came along would destroy civilization. (Gerald Weinberg)'
    elif answerNumber == 16:
        return 'There are two ways to write error-free programs; only the third one works. (Alan J. Perlis)'
    elif answerNumber == 17:
        return 'Ready, fire, aim: the fast approach to software development. Ready, aim, aim, aim, aim: the slow approach to software development. (Anonymous)'
    elif answerNumber == 18:
        return 'Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. (Martin Golding)'
    elif answerNumber == 19:
        return 'Programming is like sex. One mistake and you have to support it for the rest of your life. (Michael Sinz)'
    elif answerNumber == 20:
        return 'Deleted code is debugged code. (Jeff Sickel)'
    elif answerNumber == 21:
        return 'Walking on water and developing software from a specification are easy if both are frozen. (Edward V Berard)'
    elif answerNumber == 22:
        return 'If debugging is the process of removing software bugs, then programming must be the process of putting them in. (Edsger Dijkstra)'
    elif answerNumber == 23:
        return 'Software undergoes beta testing shortly before it’s released. Beta is Latin for “still doesn’t work. (Anonymous)'
    elif answerNumber == 24:
        return 'Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the universe trying to produce bigger and better idiots. So far, the universe is winning. (Rick Cook)'
    elif answerNumber == 25:
        return 'It’s a curious thing about our industry: not only do we not learn from our mistakes, but we also don’t learn from our successes. (Keith Braithwaite)'
    elif answerNumber == 26:
        return 'There are only two kinds of programming languages: those people always bitch about and those nobody uses. (Bjarne Stroustrup)'
    elif answerNumber == 27:
        return 'In order to understand recursion, one must first understand recursion. (Anonymous)'
    elif answerNumber == 28:
        return 'The cheapest, fastest, and most reliable components are those that aren’t there. (Gordon Bell)'
    elif answerNumber == 29:
        return 'The best performance improvement is the transition from the nonworking state to the working state. (J. Osterhout)'
    elif answerNumber == 30:
        return 'The trouble with programmers is that you can never tell what a programmer is doing until it’s too late. (Seymour Cray)'
    elif answerNumber == 31:
        return 'Don’t worry if it doesn’t work right. If everything did, you’d be out of a job. (Mosher’s Law of Software Engineering)'
r = random.randint(1, 31)
quote = getAnswer(r)

weather_api=os.getenv("WEATHERAPI")
#print(weather_api)

owm = OWM(weather_api)
mgr = owm.weather_manager()
weather = mgr.weather_at_place('Grand Rapids, US').weather
temp_dict_kelvin = weather.temperature()   # a dict in Kelvin units (default when no temperature units provided)
d = weather.temperature('fahrenheit')

#print(d)
c = d.get('temp')
h = d.get('temp_max')
lo = d.get('temp_min')
f = d.get('feels_like')

#string conversion
currenttemp = str(c)
high = str(h)
low = str(lo)
feels = str(f)
#print(currenttemp)

ct = datetime.now().strftime('%H:%M:%S')

def timeframe():
    if ct >= '00:00:00' and ct <= '11:59:59':
        return 'Good Morning, '
    elif ct >= '12:00:00' and ct <= '16:59:59':
        return 'Good Afternoon, '
    elif ct >= '17:00:00' and ct <= '23:59:59':
        return 'Good Evening, '
currentTime = timeframe()

statusquote = (currentTime+ 'the current temperature in Grand Rapids is '+currenttemp+' deg. fahrenheit.')

# Create a tweet
logger.info("Posting Tweet")
api.update_status(statusquote+' Quote of the day: '+quote+" #pythonprogramming #python #programming #developer")
print("Tweet Sent: "+ statusquote+' Quote of the day: '+quote+" #pythonprogramming #python #programming #developer")
