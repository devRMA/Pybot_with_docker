# Definindo a imagem base
FROM python:3.9.7

# usando o output unbuffered para conseguir olhar os logs pelo docker
# https://github.com/moby/moby/issues/12447#issuecomment-93932924
ENV PYTHONUNBUFFERED 1

# Baixando as dependências do bot
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Criando um usuário
RUN useradd -ms /bin/bash bot
USER bot

ENTRYPOINT ["python"]