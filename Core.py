import discord
import time 
import random
import os
import time
from threading import *


client = discord.Client()
token = ""

@client.event
async def on_message(message):
    if message.author.id in [12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345, 12345]:
        await message.channel.trigger_typing()
        time.sleep(0.01)
        await message.channel.send(random.choice([
   print(f"Readyy")

client.run(token, bot=False)
