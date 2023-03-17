import discord
import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
TOKEN = os.getenv('TOKEN')

app = Flask(__name__)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        username = str(message.author)
        user_message = str(message.content).lower()
        channel = str(message.channel.name)

        if username == self.user:
            print("self")
            return

        if user_message == 'hi':
            await message.channel.send('Hello')
            return

        return


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)

