import discord

token = open("token.txt", "r").read()
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    msg = ''
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if str(message.author) == "Anderson Programmer#2568":
        msg = ' Professor'
    if "hello lefty" in message.content.lower():
        await message.channel.send('Hello' + msg + ', how may I help?')
    if "tv remote" in message.content.lower():
        await message.channel.send('Sorry' + msg + ', I am an intangible entity and cannot perform physical tasks.')

client.run(token)