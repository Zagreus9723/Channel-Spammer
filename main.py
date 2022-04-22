import discum
import json
import time
bot = discum.Client(token=f'{input("Input token: ")}', log=False)
message = input("Input message: ")
channel = input("Input channel ID: ")
while True:
  time.sleep(1)
  bot.sendMessage(f"{channel}",f"{message}")
