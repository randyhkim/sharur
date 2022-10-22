# import youtube_dl
# from discord import FFmpegPCMAudio
#
#
# @bot.command
# async def play(ctx, url:str):
#     if(ctx.author.voice):
#         channel = ctx.message.author.voice.channel
#         voice = await channel.connect()
#
#         ydl_opts = {
#             'format': 'bestaudio/best',
#             'postprocessors': [{
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '192',
#             }]
#         }
#
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#         for file in os.listdir("./"):
#             if file.endswidth(".mp3"):
#                 os.rename(file, "song.mp3")
#
#         source = FFmpegPCMAudio('song.mp3')
#         player = voice.play(source)
#     else:
#         await ctx.send("I am not in a voice channel!")


