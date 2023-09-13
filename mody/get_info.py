from asyncio import get_event_loop

from pyrogram import Client


async def getBot_token():
    try:
        from info import token
        bot = Client('MainBot', 25996320, '772cefc3a92ed382b6c24adbd0d3ea26',
                     no_updates=True, in_memory=True, bot_token=token)
        await bot.start()
    except:
        token = '6508478679:AAEu-xxKzguEs-sbLaEbARsyX4jYutihye0'
    try:
        from info import sudo_username
        get_sudo = await bot.get_chat(sudo_username)
    except:
        sudo_username = '@T_4IJ'
    try:
        from info import user_bot
        get_bot_tmwel = await bot.get_chat(user_bot)
    except:
        user_bot = '@BOYR5BOT'
    try:
        from info import sudo_id
    except:
        file = open('info.py', 'a')
        file.write(f'sudo_id = {get_sudo.id}\n')
        file.close()
    get_bot = await bot.get_me()
    await bot.stop()
    return token, get_sudo, get_bot, get_bot_tmwel


token, sudo_info, get_bot, get_bot_tmwel = get_event_loop().run_until_complete(getBot_token())

