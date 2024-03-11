import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '+', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Success')

@client.command()
async def hello(ctx):
    await ctx.send('hello!')

@client.command()
async def goodbye(ctx):
    await ctx.send('bye~')

client.run('MTIxNjQyNjY2ODg1NjcwOTE5MA.G9TtmZ.RatyNIj6u2HyrecYIU84oQbtC72FAWiFfNKCdg')

