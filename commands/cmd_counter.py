import general
import discord
from cmdreqfiles import counterfile

client = general.client


@client.command(aliases=["co"])
async def counter(ctx, counterhero):
    embed = discord.Embed(
        title='Overwatch Counterhero',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='Manuell copied from: https://www.esportstales.com/overwatch/hero-counter-list')
    embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/994151684057321473/JSWK6C4w_400x400.jpg')

    if counterhero.lower() in counterfile.items:
        embed.add_field(name=counterhero.upper() + ' Counter', value=counterfile.counterselector(counterhero.lower()), inline=False)
        await ctx.channel.send(embed=embed)
    else:
        wrong = ''
        embed.add_field(name='Diesen Helden gibt es nicht!', value='Hier ist eine Liste der verfügbaren Helden', inline=False)
        for x in counterfile.items:
            wrong += x + '\n'

        embed.add_field(name='Herolist', value=wrong, inline=False)
        await ctx.author.send(embed=embed)


@counter.error
async def counter(ctx, error):
    await ctx.send("Gib einen Helden an")
    print(error)

