import discord
import time


print(
"""

               _     _                 _                                                    
              | |   | |               | |                                                   
 __      _____| |__ | |__   ___   ___ | | __  ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
  \ V  V /  __/ |_) | | | | (_) | (_) |   <  \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
   \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                 | |                                        
                                                 |_|        diuwuv3/webhookspammer                     
                                                                      
"""
)


webhookurl = input("Webhook URL? ")
username = input("Webhook username (optional)? ")
avatar = input("Webhook avatar (optional)? ")
message = input("Message? ")
delay = float(input("Delay? "))
webhook = discord.Webhook.from_url(webhookurl, adapter=discord.RequestsWebhookAdapter())


print("\nPress CTRL-C to stop...")
while True:
    webhook.send(content=message, username=username, avatar_url=avatar)
    print("[!] Message sent!")
    time.sleep(delay)