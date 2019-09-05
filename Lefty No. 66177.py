import discord
from discord.ext import commands

TOKEN = open("token.txt", "r").read()
bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print("Lefty No. 66177 Online")

@bot.event
async def on_message(message):
    print(f"{message.author.name}: {message.content}")
    if message.author == bot.user:
        return
    prof = ""
    if str(message.author) == "Anderson Programmer#2568":
        prof = " Professor"
    if "hello lefty" in message.content.lower():
        await message.channel.send('Hello' + prof + ', how may I help?')
    if ">echo" in message.content:
        x = message.content.split(" ", 1)
        await message.channel.send(x[1])

@bot.command()
async def echo(ctx):
    print("help plz")

bot.run(TOKEN)