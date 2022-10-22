# sharur

Sharur is a multipurposed discord bot that can get Youtube videos and play it in a voice chat so music can be shared among users. In addition to music, it can also store important reminders that can remind one to everyone in the server so that nobody misses any events or important dates that is not in calendars.
If on windows, install ffmpeg manually by downloading the ffmpeg executable file and putting it in the scripts folder. https://stackoverflow.com/questions/30770155/ffprobe-or-avprobe-not-found-please-install-one

## Functions
### $join and $leave
https://user-images.githubusercontent.com/63735714/197359114-48737b9b-537b-473f-a112-994ce9e35876.mov

`$join` commands the Sharur bot to join the channel the user is at. If the user is in no channel, the bot declines, saying "I am not in a voice channel!" `$leave` commands the bot to leave the channel.


### $play
https://user-images.githubusercontent.com/63735714/197361733-b1885863-2421-4465-9cec-deafd9eac78e.mov

`$play` allows user to input a Youtube video link and the Discord bot will automatically join the voice channel and play the audio of that Youtube video. If you call `$play` again, the music being played will be aborted and the audio of the new Youtube video will be played immediately.


### $ping
https://user-images.githubusercontent.com/63735714/197359135-2d7c5e50-cb08-4c47-816c-7a65a070d890.mov

`$ping` is a command that returns a message saying "pong" as a demonstration purpose for development.

### $add_birthday
https://user-images.githubusercontent.com/63735714/197359620-6307a4c0-38b9-4797-920f-4c449d8657ff.mov


`$add_birthday` allows user to interactively add an entry to the birthday database. If any of the inputs are invalid, the bot will return an "Internal server error." response. If the user fails to respond within 30 seconds since the last prompt, the interaction is aborted.
When successful, a rich, embedded Discord message highlights that the addition was successful.


### $remove_birthday
https://user-images.githubusercontent.com/63735714/197359129-8849ccdf-b7a3-4b93-b560-653ff883e590.mov

`$remove_birthday` removes all birthday entries with the name inputted by the user. If none is found or the input is invalid, the bot will return an "Internal server error." response. If the user fails to respond within 30 seconds since the last prompt, the interaction is aborted.
When successful, a rich, embedded Discord message highlights that the removal was successful.


### $fetch_birthdays
https://user-images.githubusercontent.com/63735714/197359126-91293d03-89a0-4937-878c-f333973167c8.mov

`$fetch_birthdays` returns a list of tuples where each tuple represents all rows in the birthday database. This function is left for development purposes.

### $birthdays_today
https://user-images.githubusercontent.com/63735714/197359123-f2e806e0-fa65-4e35-afc4-3bfb7df1587d.mov

`$birthdays_today` tags `@everyone` and returns a rich, embedded Discord message that highlights people whose birthday is today, along with the birthday message that was written when creating the birthday database entry.

