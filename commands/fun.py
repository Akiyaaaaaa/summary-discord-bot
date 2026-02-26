from __future__ import annotations

import logging

from discord import app_commands
import discord
from discord.ext import commands

from services.ai_service import GeminiService
from utils.chat_utils import get_chat_history, truncate

log = logging.getLogger(__name__)


class Fun(commands.Cog, name="Fun"):
    def __init__(self, bot: commands.Bot, ai: GeminiService) -> None:
        self.bot = bot
        self.ai = ai

    @app_commands.command(name="roast", description="Playfully roast a user based on their messages.")
    @app_commands.describe(member="The user to roast (defaults to yourself)")
    async def roast(self, interaction: discord.Interaction, member: discord.Member = None) -> None:
        await interaction.response.defer()
        history = await get_chat_history(interaction.channel, limit=50)
        if not history:
            await interaction.followup.send("📭 No chat history to roast anyone with!")
            return

        target = member or interaction.user
        prompt = (
            "You are a witty comedian. Based on the Discord chat log below, "
            f"write a short, playful roast of the user **{target.display_name}**. "
            "Keep it light-hearted and funny — never mean-spirited, offensive, "
            "or hurtful. Max 3 sentences.\n\n"
            f"Chat log:\n{history}"
        )
        result = await self.ai.generate_response(prompt)
        await interaction.followup.send(f"🔥 **Roast of {target.display_name}:**\n{truncate(result)}")

    @app_commands.command(name="quote", description="Generate a fake-inspirational quote based on the conversation.")
    async def quote(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer()
        history = await get_chat_history(interaction.channel, limit=50)
        if not history:
            await interaction.followup.send("📭 No chat history to draw inspiration from!")
            return

        prompt = (
            "You are a satirical philosopher. Based on the Discord chat log "
            "below, generate ONE fake-inspirational quote that sounds deep "
            "but is humorously based on the actual conversation topics. "
            "Format it as:\n"
            '> "quote text"\n'
            "> — Fictional Author Name\n\n"
            f"Chat log:\n{history}"
        )
        result = await self.ai.generate_response(prompt)
        await interaction.followup.send(f"✨ **Inspirational Quote:**\n{truncate(result)}")


async def setup(bot: commands.Bot) -> None:
    ai: GeminiService = bot.ai_service
    await bot.add_cog(Fun(bot, ai))
    log.info("Cog loaded: Fun")
