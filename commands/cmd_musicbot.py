from discord import FFmpegOpusAudio
from youtube_dl import YoutubeDL

import general

client = general.client
YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': 'True', 'quiet': 'True', 'ignoreerrors': 'True'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

queue = {}


def get_info(url):
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
    return info


def check_queue(server, voiceclient):
    if server not in queue:
        return

    if queue[server]:
        print(queue[server])
        voiceclient.play(FFmpegOpusAudio(queue[server].pop(0), **FFMPEG_OPTIONS),
                         after=lambda x: check_queue(server, voiceclient))


@client.command()
async def join(ctx):
    if ctx.author.voice is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

    await ctx.author.voice.channel.connect()

    # voicechannel.play(discord.FFmpegOpusAudio(source="w.mp3"))


@client.command()
async def leave(ctx):
    if ctx.voice_client is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Der Bot befindet sich nicht in einem Voicechannel!')

    await ctx.voice_client.disconnect()


@client.command()
async def play(ctx, url: str = None):
    server = ctx.message.guild

    if ctx.author.voice is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

    if url is None or url.find("youtube.com") < 0:
        return await ctx.send('Die URL muss eine valide YouTube-URL sein!')

    voiceclient = ctx.voice_client

    if voiceclient is None:
        voiceclient = await ctx.author.voice.channel.connect()

    INFO = get_info(url)

    if not voiceclient.is_playing():
        voiceclient.play(
            FFmpegOpusAudio(INFO['formats'][0]['url'], **FFMPEG_OPTIONS),
            after=lambda x: check_queue(server.id, voiceclient)
        )
        await ctx.send(f"Spiele {INFO['title']} :notes:")
    else:

        if server.id in queue:
            queue[server.id].append([INFO['formats'][0]['url']])
        else:
            queue[server.id] = [INFO['formats'][0]['url']]

        await ctx.send("Es wird bereits ein Song abgespielt! Der Track wird der Warteschlange hinzugefügt :stopwatch: ")


@client.command()
async def next(ctx):
    if ctx.author.voice is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

    voiceclient = ctx.voice_client
    server = ctx.message.guild

    if queue[server.id]:
        voiceclient.stop()
        voiceclient.play(FFmpegOpusAudio(queue[server.id].pop(0), **FFMPEG_OPTIONS),
                         after=lambda x: check_queue(server.id, voiceclient))
    else:
        await ctx.send('Die Warteschlange ist leer!')


@client.command()
async def pause(ctx):
    if ctx.author.voice is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

    voiceclient = ctx.voice_client
    if voiceclient.is_playing():
        voiceclient.pause()
        await ctx.send('Track wird pausiert!')


@client.command()
async def resume(ctx):
    if ctx.author.voice is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

    voiceclient = ctx.voice_client
    if voiceclient.is_paused():
        voiceclient.resume()
        await ctx.send('Track wird fortgesetzt!')
