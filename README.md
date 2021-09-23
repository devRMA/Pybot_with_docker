<h1 align="center">
    Discord Bot feito com Python e docker
</h1>

## Este repositorio, é um exemplo de bot feito com o discord.py, usando PostgreSQL e Redis e Docker.

### Requisito para executar o bot

- [Docker](https://docs.docker.com/engine/install/)

### Passo a passo para executar o bot

1. Crie o arquivo ``.env`` e copie o conteúdo do arquivo ``.env.example`` para o ``.env``.
2. Coloque o token do bot, e o id da sua conta no discord.
3. Execute o docker compose

   ```shell
   docker-compose up -d
   ```

### Comandos uteis

- Para ver os logs do bot, use o comando abaixo

  ```shell
  docker-compose logs -f -t bot
  ```

  (Ou caso queira ver todos os logs, retire o "bot" do final do comando)
- Para reiniciar o bot, use o comando

  ```shell
  docker-compose restart bot
  ```

- Caso queira parar todos os containers (banco, redis e bot), use o comando

  ```shell
  docker-compose down
  ```

- Caso queira acessar o bash do bot (ou de algum outro container), use o comando

  ```shell
  docker-compose exec bot bash
  ```
