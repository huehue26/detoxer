import discord
import os
from dotenv import load_dotenv
from flask import Flask
import pickle
from mongodb import get_warning_count,update_warning_count

load_dotenv()
TOKEN = os.getenv('TOKEN')

app = Flask(__name__)

model = pickle.load(open('/Users/mac/Desktop/detox/model/model.pkl', 'rb'))
vectorizer = pickle.load(open('/Users/mac/Desktop/detox/model/vectorizer.pickle', 'rb'))


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        username = str(message.author)
        user_message = str(message.content).lower()
        channel = str(message.channel.name)

        print(user_message)

        if username == self.user:
            print("self")
            return

        msg_df = vectorizer.transform([user_message])
        model_prediction = model.predict(msg_df)

        # user_warning_count = await get_warning_count(username)
        # print(user_warning_count)

        if model_prediction[0] == 1:
            # if user_warning_count == 9:

            # await update_warning_count(username, 1, 0)
            # await message.channel.send(f'Warning!!!!! Please user appropriate language, {10-user_warning_count} until '
            #                            f'timeout')
            await message.channel.send('Warning!!!!! Please user appropriate language')
            return

        if user_message == 'hi':
            await message.channel.send('Hello')
            return

        return


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)

