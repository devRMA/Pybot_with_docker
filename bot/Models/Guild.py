from sqlalchemy import Column, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select

Base = declarative_base()


class Guild(Base):
    # o nome da tabela que esse model representa
    __tablename__ = 'guilds'
    # uma coluna com o nome "ID" que vai ser a PK
    id = Column(BigInteger, primary_key=True)
    # uma coluna "prefix" para guardar o prefixo da guild
    prefix = Column(String(4))

    def __repr__(self):
        return f'<Guild Id:{self.id} Prefix:{self.prefix}>'

    def __str__(self):
        return f'<Guild Id:{self.id} Prefix:{self.prefix}>'

    @staticmethod
    async def find(async_session, id_):
        # Método estatico que procura uma guild pelo ID no banco
        async with async_session() as session:
            stmt = select(Guild).where(Guild.id == id_)
            return (await session.execute(stmt)).scalars().first()

    async def save(self, async_session):
        # Método que salva a guild atual, no banco 
        async with async_session() as session:
            session.add(self)
            await session.commit()

    async def delete(self, async_session):
        # Exclui a guild atual do banco
        async with async_session() as session:
            await session.delete(self)
            await session.commit()

    async def update(self, async_session):
        # Atualiza o prefixo da guild atual no banco
        async with async_session() as session:
            stmt = select(Guild).where(Guild.id == self.id)
            db_guild = (await session.execute(stmt)).scalars().first()
            db_guild.prefix = self.prefix
            await session.commit()


async def create_guild_table(engine):
    # Método que cria no banco, a tabela do model Guild
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
