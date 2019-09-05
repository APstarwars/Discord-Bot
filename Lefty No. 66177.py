import discord

TOKEN = open("token.txt", "r").read()
client = discord.Client()

@client.event
async def on_ready():
    print("Lefty No. 66177 Online")

@client.event
async def on_message(message):
    print(f"{message.author.name}: {message.content}")
    if message.author == client.user:
        return
    prof = ""
    if str(message.author) == "Anderson Programmer#2568":
        prof = " Professor"
    if "hello" in message.content.lower():
        await message.channel.send('Hello' + prof + ', how may I help?')

client.run(TOKEN)