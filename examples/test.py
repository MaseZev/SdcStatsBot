from SdcStatsBot import SdcApi
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())


async def main():
    api = SdcApi(interval=60)
    await api.start_posting_stats(bot_id=1234567890,
                                  sdc_token="token_sdc_api",
                                  servers_count=439, shard_count=1)

@bot.event
async def on_ready():
    await main()

bot.run("toke bot")