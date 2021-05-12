import general

client = general.client


@client.command()
async def ping(ctx):
    await ctx.send('Current Ping: ' + str(round(client.latency * 1000)) + 'ms!')