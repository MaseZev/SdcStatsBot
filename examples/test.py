from SDcStatsBot import SdcApi
import disnake
from disnake.ext import commands
import logging

logging.basicConfig(level=logging.INFO)
bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())


async def main():
    api = SdcApi(logger=logging.getLogger(__name__), interval=60) #Update interval 60 minutes
    await api.start_posting_stats(bot_id=1234567890, # Bot Id
                                  sdc_token="token_sdc_api", # Token from the Sdc website
                                  servers_count=1000, shard_count=1) # It is not necessary to set the number of shards

@bot.event
async def on_ready():
    await main()

bot.run("token bot") # Token bot discord developer portal
