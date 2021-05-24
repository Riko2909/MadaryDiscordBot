import discord

import general

client = general.client

channellist = {}


@client.command(aliases=['cvc', 'createvoice'])
async def createVC(ctx):
    guild = ctx.message.guild
    author = ctx.message.author

    if author.voice is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

    if author.id == 341907606388080642:
        channel = await guild.create_voice_channel(f"Nicks's Pimmel ist klein",
                                                   category=discord.utils.get(guild.categories, name="Sprachkanäle", ))
    else:
        channel = await guild.create_voice_channel(f"{author.name}'s Channel",
                                                   category=discord.utils.get(guild.categories, name="Sprachkanäle", ))
    await channel.set_permissions(target=author,
                                  view_channel=True,
                                  connect=True,
                                  move_members=True,
                                  manage_channels=True,
                                  create_instant_invite=False
                                  )
    if author.voice is None:
        await channel.delete()
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

    await author.move_to(channel)
    channellist[channel.id] = author.id
    print(channellist)
    await ctx.send(f"Viel Spaß in deinem temporären Channel! {author.display_name} :)")


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None:
        return

    if before.channel == after.channel:
        return

    if channellist.get(before.channel.id) == member.id:
        channellist.pop(before.channel.id)
        print(f"Privater Channel von {member.display_name} wurde gelöscht!")
        await before.channel.delete()
