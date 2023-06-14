from hermes import Hermes
from constants import Const
import time
import random
#!/usr/bin/env python3
"""Entrypoint into the script where the arguments are passed to lib.main"""
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]

    while True:
        try:
            code="us"
            page=0
            if arguments:
                code=arguments[0]
                page=arguments[1]
            bot=Hermes(code)
            bot.checkdrops(page)
            # 生成隨機等待時間
            wait_time = random.randint(50, 70)
            time.sleep(wait_time)
            pass
        except KeyboardInterrupt:
            print("\nCtrl+C pressed. Stopping all checkins")
            sys.exit()
     