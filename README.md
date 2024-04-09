# SdcStatsBot
* Враппер на Python для [SDC API](https://docs.server-discord.com)
* Документация к API: https://docs.server-discord.com/
* [Сервер поддержки](https://discord.gg/H7FQFGEPz5) враппера 

## Установка

```
pip install SdcStatsBot
```

# Внимание!
## Враппер полностью асинхронен. Любые вызовы функций следует проводить только в асинхронных функциях

## Враппер включает в себя на данный момент 1 класс

## Использование

#### Bots

```py
from SDcStatsBot import SdcApi
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())

async def main():
    await SdcApi().post("Бот айди без кавычек", "Sdc токен", "Количество серверов без кавычек", "Количество шардов без кавычек") # Отправляет статистику каждые 30 минут

@bot.event
async def on_ready():
    await main()

bot.run("")

```
