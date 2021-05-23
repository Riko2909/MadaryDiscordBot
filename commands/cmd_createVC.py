import discord

import general

client = general.client


@client.command(aliases=['cvc', 'createvoice'])
async def createVC(ctx):
    guild = ctx.message.guild
    author = ctx.message.author

    if author.voice is None:
        # Exiting if the user is not in a voice channel
        return await ctx.send('Du musst in einem Voicechannel sein um diesen Command auszuführen!')

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
    await ctx.send("Viel Spaß in deinem temporären Channel! :)")


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None:
        return

    print(before.channel.name)
    print(f"{member.display_name}'s Channel")

    if before.channel.name == f"{member.display_name}'s Channel":
        print(f"Privater Channel von {member.display_name} wurde gelöscht!")
        await before.channel.delete()
