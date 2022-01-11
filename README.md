# Um Bot para o Discord feito com Python e Docker

## Este repositório, é um exemplo de bot feito com o discord.py, usando PostgreSQL como banco de dados, Redis como cache e Docker

### Requisito para executar o bot

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Passo a passo para executar o bot

1. Crie o arquivo ``.env``

    ```shell
    # Linux/macOS
    cp .env.example .env

    # Windows
    copy .env.example .env
    ```

2. Coloque o token do bot e o ID da sua conta no ``.env``
3. Execute o docker compose

   ```shell
   docker-compose up -d
   ```

### Comandos uteis

- Para ver os logs do bot, use o comando abaixo

  ```shell
  docker-compose logs -f -t --no-log-prefix bot
  ```

  (Caso queira ver todos os logs, retire o ``--no-log-prefix bot`` do final do comando)

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

- Para ver os containers que estão online, use o comando

  ```shell
  docker-compose ps
  ```
