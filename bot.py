import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

bot = commands.Bot(command_prefix = '=')

@bot.command()
async def join(ctx):
    channel = ctx.author.VoiceState.channel
    await channel.connect
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
