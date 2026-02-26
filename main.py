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

class MyBot(commands.Bot):
    async def setup_hook(self) -> None:
        """Async setup hook to load cogs and sync slash commands globally."""
        cogs_dir = pathlib.Path(__file__).parent / "commands"

        for filepath in sorted(cogs_dir.glob("*.py")):
            if filepath.name.startswith("_"):
                continue

            extension = f"commands.{filepath.stem}"
            try:
                await self.load_extension(extension)
                log.info("Loaded extension: %s", extension)
            except Exception as exc:
                log.error("Failed to load extension %s: %s", extension, exc, exc_info=True)
                
        # Sync slash commands globally
        log.info("Syncing slash commands...")
        await self.tree.sync()
        log.info("Slash commands synced successfully.")


bot = MyBot(
    command_prefix="/",
    intents=intents,
    description="AI-powered Discord summarizer bot using Google Gemini.",
)

bot.ai_service = GeminiService(api_key=GEMINI_API_KEY)


@bot.event
async def on_ready() -> None:
    log.info("Logged in as %s (ID: %s)", bot.user, bot.user.id)
    log.info("Connected to %d guild(s)", len(bot.guilds))
    activity = discord.Activity(
        type=discord.ActivityType.listening,
        name="/summarize | /help",
    )
    await bot.change_presence(activity=activity)


@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError) -> None:
    """Global error handler for application (slash) command exceptions."""
    command_name = interaction.command.name if interaction.command else "Unknown"
    log.error("Unhandled application command error in %s: %s", command_name, error, exc_info=error)
    
    error_msg = "❌ An unexpected error occurred. Please try again later."
    try:
        if interaction.response.is_done():
            await interaction.followup.send(error_msg, ephemeral=True)
        else:
            await interaction.response.send_message(error_msg, ephemeral=True)
    except discord.errors.InteractionResponded:
        pass

async def main() -> None:
    """Async entry point: start the bot."""
    async with bot:
        await bot.start(DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
