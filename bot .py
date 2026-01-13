import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Example slash command
@bot.slash_command(name="ping", description="Check bot latency")
async def ping(ctx):
    await ctx.respond(f"Pong! {round(bot.latency*1000)}ms")

# Example static file command
@bot.command()
async def playfile(ctx):
    file_path = os.path.join("static", "sample.mp3")
    if os.path.exists(file_path):
        await ctx.send(file=discord.File(file_path))
    else:
        await ctx.send("File not found!")

bot.run(os.getenv("MTQ2MDc1NTI1MjU1Mzk3Mzk5Ng.GJHgkc._mzpbiDmoVT_kPKDdcQr_QsmMCzofEOJDr6Jsk"))
