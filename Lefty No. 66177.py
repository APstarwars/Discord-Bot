import discord
from discord.ext import commands
import random

TOKEN = open("token.txt", "r").read()

class LeftyBot(discord.Client):
    async def on_ready(self):
        print("{0.name} Online".format(self.user))

    async def on_message(self, message):
        print("{0.author.name}: {0.content}".format(message))
        if message.author == self.user:
            return
        prof = ""
        if str(message.author) == "Anderson Programmer#2568":
            prof = " Professor"
        if ">echo" in message.content:
            x = message.content.split(" ", 1)
            await message.channel.send(x[1])
        elif ">pick" in message.content:
            x = message.content.split(" ", 1)
            y = x[1].split("|")
            await message.channel.send(y[random.randint(0, len(y)-1)])
        elif ">8ball" in message.content:
            x = random.randint(0, 7)
            if x==0:
                msg = "It is not likely"
            elif x==1:
                msg = "Perhaps, if you try hard enough"
            elif x==2:
                msg = "My calculations returned True"
            elif x==3:
                msg = "I wouldn't count on it"
            elif x==4:
                msg = "Definitely, with 99.89 percent certainty"
            elif x==5:
                msg = "Impossible with our current state of technology"
            elif x==6:
                msg = "I must apologise, I cannot say"
            elif x==7:
                msg = "That is information I cannot disclose"
            await message.channel.send(':8ball:| ' + msg + ',' + prof + ' **{0.author.name}**'.format(message))
        elif "hello lefty" in message.content.lower():
            await message.channel.send('Hello' + prof + ', how may I help?')

bot = LeftyBot()
bot.run(TOKEN)