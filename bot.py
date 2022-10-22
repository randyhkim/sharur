import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import youtube_dl
from discord import FFmpegPCMAudio


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

in_channel = False
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
        global in_channel
        in_channel = True
    else:
        await ctx.send("You're not in a voice channel!")


@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        print('it probably works2')
        await ctx.voice_client.disconnect()
        global in_channel
        in_channel = False
    else:
        await ctx.send("I am not in a voice channel!")


@bot.command()
async def play(ctx, url:str):
    if os.path.exists(os.path.abspath(".\\media") + "\\song.mp3"):
        os.remove(os.path.abspath(".\\media") + "\\song.mp3")
        print("it works")

    global in_channel
    if in_channel:
        await ctx.voice_client.disconnect()
        in_channel = False

    if ctx.author.voice:
        in_channel = True
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()

        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': './media/%(title)s.mp3',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        working_dir = os.path.abspath(".\\media")
        for file in os.listdir(working_dir):
            if file.endswith(".mp3"):
                os.rename(working_dir + "\\" + file, working_dir + "\\song.mp3")

        source = FFmpegPCMAudio(working_dir + "\\song.mp3")
        player = voice.play(source)
        if not voice.is_playing():
            os.remove(working_dir + "\\song.mp3")
    else:
        await ctx.send("You're am not in a voice channel!")


@bot.command()
async def ping(ctx):
    print('it has to work!')
    await ctx.channel.send("pong")


bot.run(TOKEN)