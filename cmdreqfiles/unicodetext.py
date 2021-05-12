stringtext = u"𝒜𝒶𝐵𝒷𝒞𝒸𝒟𝒹𝐸𝑒𝐹𝒻𝒢𝑔𝐻𝒽𝐼𝒾𝒥𝒿𝒦𝓀𝐿𝓁𝑀𝓂𝒩𝓃𝒪𝑜𝒫𝓅𝒬𝓆𝑅𝓇𝒮𝓈𝒯𝓉𝒰𝓊𝒱𝓋𝒲𝓌𝒳𝓍𝒴𝓎𝒵𝓏𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫 "
stringnormal = u"AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789 "


def changetonice(text):
    username = ""
    for chara in text:
        for i in range(63):
            if stringnormal[i] == chara:
                username += stringtext[i]
                break

    return username
