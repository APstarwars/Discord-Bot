import discord

token = open("token.txt", "r").read()
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if str(message.author) == "Anderson Programmer#2568" and "hello" in message.content.lower():
        await message.channel.send('Hello Professor, how may I help?')

client.run(token)