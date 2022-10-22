import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import youtube_dl
from discord import FFmpegPCMAudio


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
async def play(ctx, url:str):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()

        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")

        source = FFmpegPCMAudio('song.mp3')
        player = voice.play(source)
    else:
        await ctx.send("I am not in a voice channel!")


@bot.command()
async def ping(ctx):
    print('it has to work!')
    await ctx.channel.send("pong")


bot.run(TOKEN)