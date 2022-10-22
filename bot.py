import asyncio
import os
import time
import discord
from dotenv import load_dotenv
from discord.ext import commands

import reminder_handler


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


@bot.command()
async def add_birthday(ctx):
    try:
        # TODO: change ID
        id = time.time()

        await ctx.channel.send("Whose birthday is this?")
        name_response = await bot.wait_for('message', timeout=30) # 30 seconds to reply
        name = str(name_response.content)
        
        await ctx.channel.send("When is the birthday (ex. 19971118)?")
        birthday_response = await bot.wait_for('message', timeout=30) # 30 seconds to reply
        birthday = str(birthday_response.content)

        # TODO: add reminded_people
        # int_reminded_people = int(reminded_people)
        int_reminded_people = 0

        await ctx.channel.send("Add a celebration message!")
        reminder_message_response = await bot.wait_for('message', timeout=30) # 30 seconds to reply
        reminder_message = str(reminder_message_response.content)

        reminder_handler.insert_birthday(reminder_handler.pool, id, name, birthday, int_reminded_people, reminder_message)
        await ctx.channel.send("Birthday successfully added!")

    except asyncio.TimeoutError:
        await ctx.send("You didn't reply in time!")
    except:
        await ctx.send(f'Internal server error.')


@bot.command()
async def remove_birthday(ctx):

    def check(response):
        # TODO: check if name exists in database instead
        return response

    try:
        await ctx.channel.send("Whose birthday do you want to remove?")
        response = await bot.wait_for("message", check=check, timeout=30) # 30 seconds to reply
        name = str(response.content)
        reminder_handler.delete_birthday(reminder_handler.pool, name)
        await ctx.channel.send(f'Successfully removed {name}\'s birthday.')
    except asyncio.TimeoutError:
        await ctx.send("You didn't reply in time!")
    except TypeError:
        await ctx.send("That user's birthday doesn't exist!")


@bot.command()
async def fetch_birthdays(ctx):
    try:
        await ctx.channel.send(reminder_handler.fetch_birthdays(reminder_handler.pool))
    except:
        await ctx.send("Internal server error.")


bot.run(TOKEN)