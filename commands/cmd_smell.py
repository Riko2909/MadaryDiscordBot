import random
import general
import perms

client = general.client


@client.command(pass_context=True, aliases=["geruch"])
async def smell(ctx, *smell):

    if not perms.check(ctx.author, 0):
        await general.failperms(ctx, 1)
        return

    textlist = ["Uiuiui es riecht nach",
                "Was stinkt hier so nach",
                "Ein kleiner Duft von",
                "Exquisiter Geruch von"]

    msg = ""
    for i in smell:
        msg += i + " "
    await ctx.send(random.choice(textlist) + " " + str(msg))

