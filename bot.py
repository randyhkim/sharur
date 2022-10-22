import asyncio
import datetime
import os
import time
import discord
from dotenv import load_dotenv
from discord.ext import commands

import reminder_handler


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
WHEN = datetime.time(0, 0, 0)    # 12:00 AM


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

        msg = discord.Embed(
            title="Addition Successful",
            description=f"Successfully added {name}'s birthday."
        )
        await ctx.send(embed=msg)

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

        msg = discord.Embed(
            title="Removal Successful",
            description=f"Successfully removed {name}'s birthday."
        )
        await ctx.send(embed=msg)
    except asyncio.TimeoutError:
        await ctx.send("You didn't reply in time!")
    except TypeError:
        await ctx.send("That user's birthday doesn't exist!")


# TODO: remove
@bot.command()
async def fetch_birthdays(ctx):
    try:
        await ctx.channel.send(reminder_handler.get_all_birthdays(reminder_handler.pool))
    except:
        await ctx.send("Internal server error.")


@bot.command(name='birthdays_today', description='Birthdays today')
async def birthdays_today(ctx):
    try:
        today = datetime.datetime.now()
        mm = str(today.month)
        dd = str(today.day)
        rows = reminder_handler.get_birthdays_at_date(reminder_handler.pool, mm, dd)

        birthdays = []

        for row in rows:    # row is in form of tuple
            birthdays.append(f'Happy birthday {row[1]}! Your friends say: {row[4]}')

        # TODO: add functionality to change tag
        await ctx.send(content="@everyone")

        for birthday in birthdays:
            birthday_embed = discord.Embed(
                color=0x1b5656,
                title="Happy Birthday!",
                description=birthday,
            )
            await ctx.send(embed=birthday_embed)

    except:
        await ctx.send("Internal server error.")


# @bot.event
# async def on_ready():
#     try:
#         today = datetime.datetime.now()
#         mm = str(today.month)
#         dd = str(today.day)
#         rows = reminder_handler.get_birthdays_at_date(reminder_handler.pool, mm, dd)

#         birthdays = []

#         for row in rows:    # row is in form of tuple
#             birthdays.append(f'Happy birthday {row[1]}! Your friends say: {row[4]}')

#         for birthday in birthdays:
#             await ctx.send(birthday)

#     except:
#         await ctx.send("Internal server error.")


# async def called_once_a_day():
#     await bot.wait_until_ready()  # Make sure your guild cache is ready so the channel can be found via get_channel
#     channel = bot.get_channel(1)    # TODO: change arbitrary channel_id
#     await channel.send("your message here")


# async def background_task():
#     now = datetime.utcnow()
#     if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
#         tomorrow = datetime.combine(now.date() + datetime.timedelta(days=1), time(0))
#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
#         await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start 
#     while True:
#         now = datetime.utcnow() # You can do now() or a specific timezone if that matters, but I'll leave it with utcnow
#         target_time = datetime.combine(now.date(), WHEN)  # 6:00 PM today (In UTC)
#         seconds_until_target = (target_time - now).total_seconds()
#         await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
#         await called_once_a_day()  # Call the helper function that sends the message
#         tomorrow = datetime.combine(now.date() + datetime.timedelta(days=1), time(0))
#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
#         await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start a new iteration


# bot.loop.create_task(background_task())
bot.run(TOKEN)
