<![CDATA[# 🤖 Discord AI Summarizer Bot

An AI-powered Discord bot that summarizes chat history, analyzes conversations, and brings fun interactions to your server — all powered by **Google Gemini**.

---

## ✨ Features

- **📝 Summarization** — Get concise bullet-point summaries of recent chat history
- **🕐 Catch-Up** — Missed the conversation? Get a quick recap of the last _N_ hours
- **✅ Action Items** — Automatically extract to-dos and tasks from chat
- **💬 Q&A** — Ask questions about the conversation and get AI-powered answers
- **🌡️ Vibe Check** — Analyze the mood and sentiment of a chat
- **☁️ Word Cloud** — See the most frequently used words in the channel
- **🔥 Roast** — Get a playful, AI-generated roast based on someone's chat messages
- **✨ Inspirational Quotes** — Generate fake-deep quotes inspired by the conversation

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- A [Discord Bot Token](https://discord.com/developers/applications)
- A [Google Gemini API Key](https://aistudio.google.com/apikey)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/bot-dc-ai-summarize.git
   cd bot-dc-ai-summarize
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   DISCORD_TOKEN=your_discord_bot_token
   GEMINI_API_KEY=your_gemini_api_key
   ```

4. **Run the bot**

   ```bash
   python main.py
   ```

---

## 📖 Commands

The default command prefix is **`!`**.

### Summarizer

| Command | Description |
|---|---|
| `!summarize [limit]` | Summarize the last _limit_ messages (default: 50) |
| `!catchup [hours]` | Get a recap of the last _hours_ hours (default: 1) |
| `!todos [limit]` | Extract action items from the last _limit_ messages (default: 100) |

#### Examples

```
!summarize
```
> 📝 **Chat Summary:**
> - The team discussed the new landing page design
> - Alex shared mockups and received feedback on color choices
> - A deadline was set for Friday

```
!summarize 200
```
> Summarizes the last 200 messages instead of the default 50.

```
!catchup
```
> 🕐 **Catch-Up (last 1.0h):**
> Not much happened — just a quick discussion about lunch plans and a couple of memes.

```
!catchup 4
```
> Catches you up on everything from the last 4 hours.

```
!todos
```
> ✅ **Action Items:**
> 1. @Alex — finalize the homepage mockup by Friday
> 2. @Jordan — review the PR for the auth module
> 3. @Sam — update the deployment docs

---

### Analysis

| Command | Description |
|---|---|
| `!ask <question>` | Ask a question about the chat history |
| `!vibe [limit]` | Analyze the mood/sentiment of the last _limit_ messages (default: 50) |
| `!wordcloud [limit]` | Show the top 15 most-used words from the last _limit_ messages (default: 100) |

#### Examples

```
!ask Who suggested the new feature?
```
> 💬 **Answer:**
> Based on the chat log, it was **Jordan** who first suggested adding dark mode support around 2 PM.

```
!vibe
```
> 🌡️ **Vibe Check:**
> 🔥 **Hyped & chaotic** — The chat is full of energy! Lots of excitement about the upcoming release, with a few friendly debates sprinkled in.

```
!vibe 200
```
> Analyzes the vibe of the last 200 messages.

```
!wordcloud
```
> ☁️ **Word Cloud:**
> **deploy** — 23
> **backend** — 18
> **bug** — 15
> **fix** — 14
> **meeting** — 12
> **update** — 11
> ...

---

### Fun

| Command | Description |
|---|---|
| `!roast [@user]` | Playfully roast a user based on their messages (defaults to yourself) |
| `!quote` | Generate a fake-inspirational quote based on the conversation |

#### Examples

```
!roast
```
> 🔥 **Roast of Alex:**
> Alex types like they're being charged per vowel. Every message is a speed-run through the English language.

```
!roast @Jordan
```
> 🔥 **Roast of Jordan:**
> Jordan's contribution to the chat is 90% emojis and 10% "lol". Truly the Shakespeare of our time.

```
!quote
```
> ✨ **Inspirational Quote:**
> > "In the grand tapestry of life, sometimes you are the deploy, and sometimes you are the bug."
> > — Sir Reginald von Stacktrace

---

## 📁 Project Structure

```
bot-dc-ai-summarize/
├── main.py                 # Bot entry point & event handlers
├── commands/
│   ├── summarizer.py       # Summarize, catch-up, and to-do commands
│   ├── analysis.py         # Ask, vibe check, and word cloud commands
│   └── fun.py              # Roast and quote commands
├── services/
│   └── ai_service.py       # Google Gemini API wrapper
├── utils/
│   └── chat_utils.py       # Chat history fetching & text utilities
├── requirements.txt
└── .env                    # Environment variables (not committed)
```

---

## 🛠️ Tech Stack

- **[discord.py](https://discordpy.readthedocs.io/)** — Discord API wrapper
- **[Google Gemini](https://ai.google.dev/)** (`gemini-1.5-flash`) — AI model for text generation
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — Environment variable management

---

## ⚙️ Configuration

| Variable | Description |
|---|---|
| `DISCORD_TOKEN` | Your Discord bot token |
| `GEMINI_API_KEY` | Your Google Gemini API key |

The AI model uses `gemini-1.5-flash` with a temperature of `0.7` and a max output of `2048` tokens. These can be adjusted in `services/ai_service.py`.

---

## 📜 License

This project is open-source. Feel free to use, modify, and distribute as you see fit.
]]>
