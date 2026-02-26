from __future__ import annotations

import asyncio
import logging
import os
import pathlib

import discord
from discord.ext import commands
from dotenv import load_dotenv

from services.ai_service import GeminiService

load_dotenv()

DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN", "")
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

if not DISCORD_TOKEN:
    raise RuntimeError("DISCORD_TOKEN is missing — check your .env file.")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing — check your .env file.")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
)
log = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="/",
    intents=intents,
    description="AI-powered Discord summarizer bot using Google Gemini.",
)

bot.ai_service = GeminiService(api_key=GEMINI_API_KEY)


async def load_cogs() -> None:
    cogs_dir = pathlib.Path(__file__).parent / "commands"

    for filepath in sorted(cogs_dir.glob("*.py")):
        if filepath.name.startswith("_"):
            continue

        extension = f"commands.{filepath.stem}"
        try:
            await bot.load_extension(extension)
            log.info("Loaded extension: %s", extension)
        except Exception as exc:
            log.error("Failed to load extension %s: %s", extension, exc, exc_info=True)


@bot.event
async def on_ready() -> None:
    log.info("Logged in as %s (ID: %s)", bot.user, bot.user.id)
    log.info("Connected to %d guild(s)", len(bot.guilds))
    activity = discord.Activity(
        type=discord.ActivityType.listening,
        name="/summarize | /help",
    )
    await bot.change_presence(activity=activity)


@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError) -> None:
    """Global error handler for command exceptions."""
    if isinstance(error, commands.CommandNotFound):
        return

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"⚠️ Missing argument: `{error.param.name}`. Use `/help {ctx.command}` for usage.")
        return

    if isinstance(error, commands.BadArgument):
        await ctx.send(f"⚠️ Invalid argument. Use `/help {ctx.command}` for usage.")
        return

    log.error("Unhandled command error in %s: %s", ctx.command, error, exc_info=error)
    await ctx.send("❌ An unexpected error occurred. Please try again later.")

async def main() -> None:
    """Async entry point: load cogs then start the bot."""
    async with bot:
        await load_cogs()
        await bot.start(DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
