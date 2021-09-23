from Models.Guild import Guild


async def get_prefix(bot, message):
    """

    Args:
        bot (Bot.Bot): Instância do bot
        message (discord.Message or discord.ext.commands.context.Context): A mensagem que quer saber o prefixo do bot
        
    Returns:
        str: o prefixo do bot, para a mensagem passada

    """
    if message.guild:  # se a mensagem tiver um servidor
        session = bot.db_session
        # vai pega as informações do servidor no banco de dados
        guild = await Guild.find(session, message.guild.id)
        if guild:
            # se o servidor já existir no banco de dados
            return guild.prefix
        else:
            # se não existir
            guild = Guild()
            guild.id = message.guild.id
            guild.prefix = '!!'
            await guild.save(session)
    return ''  # se a mensagem foi enviado no privado, não vai ter prefixo
