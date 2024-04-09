from SdcStatsBot.client import SdcApi
import disnake
from disnake.ext import commands


bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())

async def main():
    await SdcApi().post("Бот айди без кавычек", "Sdc токен", "Количество серверов без кавычек", "Количество шардов без кавычек")

@bot.event
async def on_ready():
    await main()

bot.run("")
