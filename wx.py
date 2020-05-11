from wxpy import *
import datetime as dt
bot = Bot()

while True:
    if dt.datetime.now().strftime('%H:%M') == '5:20':
        my_friend = bot.friends().search('低脂咖啡')[0]
        my_friend.send('早安') 