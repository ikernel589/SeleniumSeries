from hermes import Hermes
from constants import Const
import time
import random


#with Hermes(country="us") as bot:

while True:
    try:
        bot=Hermes("us")
        bot.checkdrops()
        # 生成隨機等待時間
        wait_time = random.randint(50, 70)
        time.sleep(wait_time)
        pass
    except KeyboardInterrupt:
        print("程式已被使用者終止")
        break