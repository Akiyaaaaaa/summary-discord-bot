from __future__ import annotations

import datetime
from typing import Optional

import discord
from discord.ext import commands


async def get_chat_history(
    ctx: commands.Context,
    limit: int = 50,
    after: Optional[datetime.datetime] = None,
) -> str:
    """
    Fetch recent messages from the current channel and return them as a
    formatted plain-text log.

    Parameters
    ----------
    ctx : commands.Context
        The invocation context (used to access the channel).
    limit : int, optional
        Maximum number of messages to retrieve (default 50, capped at 500).
    after : datetime.datetime | None, optional
        If provided, only fetch messages sent after this UTC timestamp.

    Returns
    -------
    str
        A newline-separated string in the format ``Username: message content``.
        Bot messages and empty messages are excluded.
    """
    limit = min(limit, 500)

    messages: list[discord.Message] = []
    async for msg in ctx.channel.history(limit=limit, after=after, oldest_first=True):
        if msg.author.bot or not msg.content:
            continue
        messages.append(msg)

    if not messages:
        return ""

    lines = [f"{msg.author.display_name}: {msg.content}" for msg in messages]
    return "\n".join(lines)


def truncate(text: str, max_length: int = 1900) -> str:
    """
    Truncate *text* so it fits inside a single Discord message (2 000 chars).

    We default to 1 900 to leave room for any surrounding formatting the
    caller might add.
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."
