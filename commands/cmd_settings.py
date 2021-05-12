import general
import perms
import json
client = general.client


def findbool(item):
    if item.lower() in ['true', '1']:
        return True
    else:
        return False


@client.command(pass_context=True)
async def settings(ctx, setting='', value='', valuetwo=''):
    if not perms.check(ctx.author, 2):
        await general.failperms(ctx, 2)
        return

    with open(general.settings) as f:
        setin = json.load(f)
        f.close()

    if not setting:
        await general.info(ctx, setin)
    else:
        if value:
            if setting == 'pretty':
                setin["pretty"] = findbool(value)
                pass
            if setting == 'add':
                if value in setin["perms"]:
                    setin["perms"][value].append(valuetwo)
                    pass
                else:
                    await general.info(ctx, setin)
            if setting == 'remove':
                if value in setin["perms"] and len(setin["perms"][value]) > 1:
                    setin["perms"][value].remove(valuetwo)
                else:
                    await general.adminsetting(ctx, 'Die Mindestanzahl der Ränge darf 1 nicht unterschreiten')
        else:
            await general.info(ctx, setin)

        fe = open(general.settings, "w")

        print(setin)
        fe.write(json.dumps(setin, indent=2))
        fe.close()


@settings.error
async def settings(ctx, error):
    print(error)