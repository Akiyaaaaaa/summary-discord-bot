from __future__ import annotations

import logging

from discord.ext import commands

from services.ai_service import GeminiService
from utils.chat_utils import get_chat_history, truncate

log = logging.getLogger(__name__)


class Fun(commands.Cog, name="Fun"):
    def __init__(self, bot: commands.Bot, ai: GeminiService) -> None:
        self.bot = bot
        self.ai = ai

    @commands.command(name="roast")
    async def roast(self, ctx: commands.Context, member: commands.MemberConverter = None) -> None:
        async with ctx.typing():
            history = await get_chat_history(ctx, limit=50)
            if not history:
                await ctx.send("📭 No chat history to roast anyone with!")
                return

            target = member or ctx.author
            prompt = (
                "You are a witty comedian. Based on the Discord chat log below, "
                f"write a short, playful roast of the user **{target.display_name}**. "
                "Keep it light-hearted and funny — never mean-spirited, offensive, "
                "or hurtful. Max 3 sentences.\n\n"
                f"Chat log:\n{history}"
            )
            result = await self.ai.generate_response(prompt)
            await ctx.send(f"🔥 **Roast of {target.display_name}:**\n{truncate(result)}")

    @commands.command(name="quote")
    async def quote(self, ctx: commands.Context) -> None:
        async with ctx.typing():
            history = await get_chat_history(ctx, limit=50)
            if not history:
                await ctx.send("📭 No chat history to draw inspiration from!")
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
            await ctx.send(f"✨ **Inspirational Quote:**\n{truncate(result)}")


async def setup(bot: commands.Bot) -> None:
    ai: GeminiService = bot.ai_service
    await bot.add_cog(Fun(bot, ai))
    log.info("Cog loaded: Fun")
