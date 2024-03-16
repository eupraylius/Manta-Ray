#accessing discord library
import discord
import asyncio
from discord.ext import commands,tasks
import random
from itertools import cycle

#initialising
client = commands.Bot(command_prefix = '+', intents=discord.Intents.all())
bot_status=cycle(["Welcome to Arbor Astralis", "My prefix is '+'", "Slaying"])

#setting up
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#hello
@client.command()
async def hello(ctx):
    await ctx.send('hello!')

#goodbye
@client.command()
async def goodbye(ctx):
    await ctx.send('bye~')

#status of the bot

@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))
    change_status.start()

# 8ball
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+8ball'):
        response = magic_8_ball()
        await message.channel.send(response)

def magic_8_ball():
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    return random.choice(responses)

#------------------:kek_slay:------------------------------
#scheduling pings
async def scheduled_message():
    await client.wait_until_ready()
    target_channel_id = 1180406985292791838 #test page 2 of the test server
    target_channel = client.get_channel(target_channel_id)
    target_role_id = 1218583043149926451 #anime news role of the test server
#------------------------------------------------
    


client.run('BOT TOKEN')

