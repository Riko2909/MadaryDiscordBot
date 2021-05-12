import json
import discord
import general
from commands import cmd_ping, cmd_counter, cmd_clear, cmd_settings, cmd_rdmhero, cmd_smell
from cmdreqfiles import unicodetext
import os

client = general.client
# token = "Njk0NjI4NDMwMjA1MDI2MzU4.XoOa1A.mBCNZw5nYJVBeJAc8OPaWIcFf9Q"
token = "Njk0NjI4NDMwMjA1MDI2MzU4.XoOZIw.6k88ufDMwAifafbrGGluvUR7Ix0"

print(discord.__version__)

def is_ascii(s):
    return all(ord(c) < 128 for c in s)


@client.event
async def on_ready():
    print('Logged in as: ' + str(client.user.name))
    await client.change_presence(activity=discord.Game("with the Programmer"))


# If Message send
@client.event
async def on_message(message):
    print("Nachricht von " + str(message.author) + ": " + message.content)

    await client.process_commands(message)


@client.event
async def on_member_join(member):
    n = str(member)
    n = n[:len(n) - 5]
    print(n + "hat den server betreten!")

    print("Pretty: " + str(unicodetext.changetonice(n)))
    await member.edit(nick=unicodetext.changetonice(n))


@client.event
async def on_message_delete(message):
    print("Gelöschte Nachricht: " + message.content)


@client.event
async def on_message_edit(before, after):
    print("Changed message from " + before.content + " to " + after.content)


@client.event
async def on_member_update(before, after):
    # print(before.roles)
    if not before.nick and not after.nick:
        return

    with open(general.settings) as f:
        setin = json.load(f)
        f.close()

    if not setin["pretty"]:
        return

    n = after.nick
    last = before.nick

    try:
        if n:
            if is_ascii(n):
                print("Pretty: " + str(unicodetext.changetonice(n)))
                await after.edit(nick=unicodetext.changetonice(n))
            else:
                if n == last:
                    return
        else:
            await after.edit(nick=unicodetext.changetonice(before.name))

        print("-------------\nBefore: " + str(last))
        print("After: " + str(n))

    except:
        print("-------------\nPermission Denied or Other Error")


client.run(token)
