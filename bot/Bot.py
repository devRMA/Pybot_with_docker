from os import getenv

import redis
from discord import Intents
from discord.ext import commands
from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from Models.Guild import create_guild_table
from utils import get_prefix


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        print('Iniciando bot...')
        self.db_session = None
        self.started = False
        self.cache = None
        intents = Intents.all()

        async def _prefix_or_mention(bot, message):
            prefix = await get_prefix(bot, message)
            return commands.when_mentioned_or(prefix)(bot, message)

        kwargs['command_prefix'] = _prefix_or_mention
        kwargs['case_insensitive'] = True
        kwargs['intents'] = intents
        kwargs['strip_after_prefix'] = True
        kwargs['owner_id'] = getenv('OWNER_ID')
        super().__init__(*args, **kwargs)
        self.load_extension('jishaku')

    async def on_ready(self):
        if not self.started:
            user = getenv('DB_USER')
            pw = getenv('DB_PASS')
            host = getenv('DB_HOST')
            port = getenv('DB_PORT')
            db_name = getenv('DB_NAME')
            dsn = f'postgresql+asyncpg://{user}:{pw}@{host}:{port}/{db_name}'
            engine = create_async_engine(
                dsn
            )

            def has_guild_table(conn):
                inspector = inspect(conn)
                return inspector.has_table('guilds')

            async with engine.connect() as conn:
                if not await conn.run_sync(has_guild_table):
                    await create_guild_table(engine)
            async_session = sessionmaker(
                engine,
                autocommit=False,
                expire_on_commit=False,
                class_=AsyncSession
            )

            self.db_session = async_session
            self.cache = redis.StrictRedis(host=getenv('REDIS_HOST', 'cache'), port=6379, db=0)
            self.cache.set('commands', 0)
            self.started = True
            print('Bot online!')
            print(f'Conta: {self.user}')
            print(f'ID: {self.user.id}')
            print('------')

    async def on_message(self, message):
        if not self.started:
            return
        ctx = await self.get_context(message)
        if message.content.replace('!', '') == self.user.mention.replace('!', ''):
            prefix = await get_prefix(self, message)
            if prefix != '':
                return await ctx.send(f'My current prefix here is: `{prefix}`')
        if ctx.valid:
            current_commands = self.cache.get('commands')
            self.cache.set('commands', int(current_commands) + 1)
            await self.invoke(ctx)
