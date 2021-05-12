import general
import perms

client = general.client


@client.command(pass_context=True, aliases=["cls", "cl"])
async def clear(ctx, amount=5):
    messages = []

    if not perms.check(ctx.author, 1):
        await general.failperms(ctx, 1)
        return

    histo = await ctx.channel.history(limit=50).flatten()
    for i in histo:
        messages.append(i)

    if amount > len(messages):
        amount = len(messages)

    await ctx.channel.purge(limit=amount)
    await ctx.send(str(amount) + " Nachrichten gelöscht :smile:")

