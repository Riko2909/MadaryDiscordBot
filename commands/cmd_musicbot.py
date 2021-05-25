from discord import FFmpegOpusAudio
from youtube_dl import YoutubeDL

import general
import discord
import youtube_dl

client = general.client
YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': 'True', 'quiet': 'True'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

queue = {}


def getPlayableURl(url):
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
    return info['formats'][0]['url']


@client.command()
async def join(ctx):
    if ctx.author.voice is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

    await ctx.author.voice.channel.connect()

    # voicechannel.play(discord.FFmpegOpusAudio(source="w.mp3"))


@client.command()
async def stop(ctx):
    if ctx.author.voice is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

    await ctx.voice_client.disconnect()


def check_queue(server, voiceclient):

    if queue[server]:
        print(queue[server])
        voiceclient.play(FFmpegOpusAudio(queue[server].pop(0), **FFMPEG_OPTIONS), after=lambda x: check_queue(server, voiceclient))



@client.command()
async def play(ctx, url: str):

    server = ctx.message.guild

    if ctx.author.voice is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

    if url is None or url.find("youtube.com") < 0:
        return await ctx.send('Die URL muss eine valide YouTube-URL sein!')

    voiceclient = ctx.voice_client

    if voiceclient is None:
        voiceclient = await ctx.author.voice.channel.connect()

    URL = getPlayableURl(url)

    if not voiceclient.is_playing():
        voiceclient.play(FFmpegOpusAudio(URL, **FFMPEG_OPTIONS), after=lambda x: check_queue(server.id, voiceclient))
    else:

        if server.id in queue:
            queue[server.id].append(URL)
        else:
            queue[server.id] = [URL]

        await ctx.send("Already playing song! Adding to queue")

@client.command()
async def next(ctx):
    if ctx.author.voice is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

    voiceclient = ctx.voice_client
    voiceclient.stop()