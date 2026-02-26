from __future__ import annotations

import logging

from discord import app_commands
import discord
from discord.ext import commands

from services.ai_service import GeminiService
from utils.chat_utils import get_chat_history, truncate

log = logging.getLogger(__name__)


class Analysis(commands.Cog, name="Analysis"):

    def __init__(self, bot: commands.Bot, ai: GeminiService) -> None:
        self.bot = bot
        self.ai = ai

    @app_commands.command(name="ask", description="Ask a question based on recent chat history.")
    @app_commands.describe(question="The question you want to ask")
    async def ask(self, interaction: discord.Interaction, question: str) -> None:
        await interaction.response.defer()
        history = await get_chat_history(interaction.channel, limit=100)
        if not history:
            await interaction.followup.send("📭 No chat history available to base an answer on.")
            return

        prompt = (
            "You are a helpful assistant with access to a Discord chat log. "
            "Answer the user's question based ONLY on the chat log below. "
            "If the answer isn't in the log, say so.\n\n"
            f"Chat log:\n{history}\n\n"
            f"Question: {question}"
        )
        result = await self.ai.generate_response(prompt)
        await interaction.followup.send(f"💬 **Answer:**\n{truncate(result)}")

    @app_commands.command(name="vibe", description="Analyze the mood/sentiment of the recent chat.")
    @app_commands.describe(limit="Maximum number of messages to analyze (default 50)")
    async def vibe(self, interaction: discord.Interaction, limit: int = 50) -> None:
        await interaction.response.defer()
        history = await get_chat_history(interaction.channel, limit=limit)
        if not history:
            await interaction.followup.send("📭 No messages found to vibe-check.")
            return

        prompt = (
            "You are a sentiment-analysis expert. Analyse the overall mood "
            "and vibe of the following Discord chat log. Give a short, fun "
            "verdict (e.g. '🔥 Hyped & chaotic') followed by a brief "
            "explanation.\n\n"
            f"Chat log:\n{history}"
        )
        result = await self.ai.generate_response(prompt)
        await interaction.followup.send(f"🌡️ **Vibe Check:**\n{truncate(result)}")

    @app_commands.command(name="wordcloud", description="Show the most-used words in recent chat messages.")
    @app_commands.describe(limit="Maximum number of messages to analyze (default 100)")
    async def wordcloud(self, interaction: discord.Interaction, limit: int = 100) -> None:
        await interaction.response.defer()
        history = await get_chat_history(interaction.channel, limit=limit)
        if not history:
            await interaction.followup.send("📭 No messages found for a word cloud.")
            return

        prompt = (
            "You are a data analyst. Analyse the following Discord chat log "
            "and produce a text-based 'word cloud'. List the top 15 most "
            "frequently used meaningful words (ignore stop-words like 'the', "
            "'is', 'a') along with their approximate count. Format each word "
            "on its own line as: **word** — count\n\n"
            f"Chat log:\n{history}"
        )
        result = await self.ai.generate_response(prompt)
        await interaction.followup.send(f"☁️ **Word Cloud:**\n{truncate(result)}")


async def setup(bot: commands.Bot) -> None:
    ai: GeminiService = bot.ai_service
    await bot.add_cog(Analysis(bot, ai))
    log.info("Cog loaded: Analysis")
