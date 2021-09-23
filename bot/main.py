from os import getenv

from discord.ext import commands
from stopwatch import Stopwatch

from Bot import Bot
from Models.Guild import Guild

bot = Bot()
token = getenv('TOKEN')


@bot.command(name='ping')
async def _ping(ctx):
    # Comando para testar se o bot está funcionando
    response_time = Stopwatch()
    msg = await ctx.send('pong')
    response_time.stop()

    db_time = Stopwatch()
    await Guild.find(bot.db_session, ctx.guild.id)
    db_time.stop()
    await msg.edit(content=f'API Latency: `{int(bot.latency * 1000)}ms`\n'
                           f'Discord Response Time: `{response_time}`\n'
                           f'Database Response Time: `{db_time}`')


@bot.command(name='setprefix', aliases=['set_prefix', 'change_prefix', 'prefix'])
@commands.guild_only()
async def _setprefix(ctx, *, prefix=None):
    # Comando simples para trocar o prefixo, com o intuito de testar o banco de dados
    if (len(prefix) > 4) or (not ctx.channel.permissions_for(ctx.author).manage_messages) or (prefix is None):
        return await ctx.send('<:lab_peepocafe:469880805624119327>')
    guild = await Guild.find(bot.db_session, ctx.guild.id)
    guild.prefix = prefix
    await guild.update(bot.db_session)
    await ctx.send(f'Prefix changed successfully to `{prefix}`!')


@bot.command('commands')
async def _commands(ctx):
    # comando que conta quantos comandos já foram usados, com o intuito de testar o redis
    count_commands = int(bot.cache.get('commands'))
    await ctx.send(f'{count_commands} command(s) have been used since I last logged in!')


bot.run(token)
