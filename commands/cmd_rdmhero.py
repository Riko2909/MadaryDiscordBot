import discord
from general import client
from cmdreqfiles import counterfile
import random


@client.command(aliases=['rdm', 'r'])
async def rdmhero(ctx):
    herolist = []
    for i in counterfile.items:
        herolist.append(i)

    newhero = random.choice(herolist)

    embed = discord.Embed(
        title='Overwatch Randomhero',
        colour=discord.Colour.blue()
    )

    embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/994151684057321473/JSWK6C4w_400x400.jpg')
    embed.add_field(name='Dein neuer Held ist: ', value=newhero.upper())
    await ctx.channel.send(embed=embed)


@rdmhero.error
async def rdmhero(ctx, error):
    print(error)
