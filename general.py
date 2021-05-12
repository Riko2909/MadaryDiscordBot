from discord.ext import commands
import discord
client = commands.Bot(command_prefix=".")
# settings = "/home/Phython/discord-bot/settings.json"
settings = "settings.json"


async def failperms(ctx, lvl):
    embedfailperms = discord.Embed(
        title='Fehlende Berechtigung',
        colour=discord.Colour.red(),
        description='Der Command ' + str(
            ctx.message.content) + ' kann nur von einem Benutzer mit dem Berechtigungslevel ' + str(
            lvl) + ' ausgeführt werden!'
    )
    await ctx.send(embed=embedfailperms)


async def adminsetting(ctx, msg):
    embedfailperms = discord.Embed(
        title='Admin Einstellungen',
        colour=discord.Colour.red(),
        description=msg
    )
    await ctx.send(embed=embedfailperms)


def converttocode(msg):
    msg = '```' + str(msg) + '```'
    return msg


async def info(ctx, dlist):
    embed = discord.Embed(
        title='Admin Einstellungen',
        colour=discord.Colour.red(),
        description='Stelle hier die gewünschten Einstellungen ein'
    )
    embed.add_field(name='Verschönerte Schrift',
                    value='SYNTAX: .settings [ pretty ] [ true | false ]\n' + converttocode(dlist["pretty"]),
                    inline=False)
    embed.add_field(name='\nRänge', value='SYNTAX: .settings [ add | remove ] [ lvl1 | lvl2 | lvl3 ] [ rank ]\n',
                    inline=False)
    for i in dlist["perms"]:
        embed.add_field(name=str(i) + '-Rank', value=converttocode(dlist["perms"][i]), inline=True)
    await ctx.channel.send(embed=embed)
