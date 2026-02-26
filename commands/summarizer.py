from __future__ import annotations

import datetime
import logging

from discord.ext import commands

from services.ai_service import GeminiService
from utils.chat_utils import get_chat_history, truncate

log = logging.getLogger(__name__)


class Summarizer(commands.Cog, name="Summarizer"):
    """Commands for summarizing and extracting info from chat history."""

    def __init__(self, bot: commands.Bot, ai: GeminiService) -> None:
        self.bot = bot
        self.ai = ai

    @commands.command(name="summarize")
    async def summarize(self, ctx: commands.Context, limit: int = 50) -> None:
        async with ctx.typing():
            history = await get_chat_history(ctx, limit=limit)
            if not history:
                await ctx.send("📭 No messages found to summarize.")
                return

            prompt = (
                "You are a helpful assistant. Summarize the following Discord "
                "chat log in a clear, concise manner. Use bullet points.\n\n"
                f"Chat log:\n{history}"
            )
            result = await self.ai.generate_response(prompt)
            await ctx.send(f"📝 **Chat Summary:**\n{truncate(result)}")

    @commands.command(name="catchup")
    async def catchup(self, ctx: commands.Context, hours: float = 1.0) -> None:
        async with ctx.typing():
            after = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=hours)
            history = await get_chat_history(ctx, limit=200, after=after)
            if not history:
                await ctx.send(f"📭 No messages found in the last **{hours}** hour(s).")
                return

            prompt = (
                "You are a helpful assistant. A user just came back and wants "
                "to catch up on what they missed. Provide a friendly, concise "
                "summary of the following Discord chat log.\n\n"
                f"Chat log (last {hours} hour(s)):\n{history}"
            )
            result = await self.ai.generate_response(prompt)
            await ctx.send(f"🕐 **Catch-Up (last {hours}h):**\n{truncate(result)}")

    @commands.command(name="todos")
    async def todos(self, ctx: commands.Context, limit: int = 100) -> None:
        async with ctx.typing():
            history = await get_chat_history(ctx, limit=limit)
            if not history:
                await ctx.send("📭 No messages found to scan for to-dos.")
                return

            prompt = (
                "You are a project-management assistant. Extract every "
                "action item, task, or to-do from the following Discord chat "
                "log. Format them as a numbered list. If there are none, say "
                "'No action items found.'\n\n"
                f"Chat log:\n{history}"
            )
            result = await self.ai.generate_response(prompt)
            await ctx.send(f"✅ **Action Items:**\n{truncate(result)}")


async def setup(bot: commands.Bot) -> None:
    ai: GeminiService = bot.ai_service
    await bot.add_cog(Summarizer(bot, ai))
    log.info("command loaded: Summarizer")
