import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())


@bot.event
async def on_ready():
    response = "connected to Discord!"
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.author.voice.channel
        print('it probably works')
        await channel.connect()
    else:
        await ctx.send("You're not in a voice channel!")


@bot.command()
async def leave(ctx):
    if(ctx.voice_client):
        print('it probably works2')
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I am not in a voice channel!")




@bot.command()
async def ping(ctx):
    print('it has to work!')
    await ctx.channel.send("pong")


bot.run(TOKEN)