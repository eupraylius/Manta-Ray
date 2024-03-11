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

client.run(TOKEN)

