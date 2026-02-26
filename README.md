<div align="center">
  <h1>🤖 Discord AI Summarizer Bot</h1>
  <p>An AI-powered Discord bot that summarizes chat history, analyzes conversations, and brings fun interactions to your server — all powered by <b>Google Gemini</b>.</p>

  [![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
  [![Discord](https://img.shields.io/badge/Discord.py-2.3.0+-5865F2.svg?logo=discord&logoColor=white)](https://discordpy.readthedocs.io/)
  [![Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-4285F4.svg?logo=google&logoColor=white)](https://ai.google.dev/)
  [![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

---

## ✨ Features

- **📝 Summarization** — Get concise bullet-point summaries of recent chat history
- **🕐 Catch-Up** — Missed the conversation? Get a quick recap of the last _N_ hours
- **✅ Action Items** — Automatically extract to-dos and tasks from the chat
- **💬 Q&A** — Ask questions about the conversation and get AI-powered answers
- **🌡️ Vibe Check** — Analyze the mood and sentiment of a chat
- **☁️ Word Cloud** — See the most frequently used words in the channel
- **🔥 Roast** — Get a playful, AI-generated roast based on someone's chat messages
- **✨ Inspirational Quotes** — Generate fake-deep quotes inspired by the conversation

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.11+** (or Docker)
- A [Discord Bot Token](https://discord.com/developers/applications) with Message Content Intent enabled
- A [Google Gemini API Key](https://aistudio.google.com/apikey)

### 🛠️ Local Installation

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

### � Running with Docker

You can easily run the bot using Docker.

1. Ensure your `.env` file is ready with your `DISCORD_TOKEN` and `GEMINI_API_KEY`.
2. Build and run the container dynamically:
   ```bash
   docker build -t discord-bot-summarize .
   docker run -d --name bot-container --restart unless-stopped --env-file .env discord-bot-summarize
   ```

### ☁️ CI/CD Deployment (GitHub Actions to GCP)

This repository includes a pre-configured GitHub Actions workflow to deploy the bot directly to a Google Cloud Platform (GCP) VM using Docker. To enable this, simply add the following **Repository Secrets** to your GitHub repository:

- `GCP_HOST`: Your VM's Public IP
- `GCP_USERNAME`: Your VM SSH username
- `GCP_SSH_KEY`: Your Private SSH key
- `DISCORD_TOKEN`: Your Discord bot token
- `GEMINI_API_KEY`: Your Gemini API key

Once configured, pushing to the `main` branch will automatically trigger a deployment to your GCP VM, seamlessly pulling your code, building the image, and spinning up the container.

---

## 📖 Commands

The default command prefix is **`/`**.

### 📝 Summarizer Commands

| Command | Description | Example |
|---|---|---|
| `/summarize [limit]` | Summarize the last _limit_ messages (default: 50) | `/summarize 100` |
| `/catchup [hours]` | Get a recap of the last _hours_ hours (default: 1) | `/catchup 2` |
| `/todos [limit]` | Extract action items from the last _limit_ messages (default: 100) | `/todos` |

### 🔍 Analysis Commands

| Command | Description | Example |
|---|---|---|
| `/ask <question>` | Ask a question about the chat history | `/ask Who suggested the new feature?` |
| `/vibe [limit]` | Analyze the mood/sentiment of the last _limit_ messages (default: 50) | `/vibe` |
| `/wordcloud [limit]` | Show the top 15 most-used words from the last _limit_ messages (default: 100) | `/wordcloud 200` |

### 🎉 Fun Commands

| Command | Description | Example |
|---|---|---|
| `/roast [@user]` | Playfully roast a user based on their messages (defaults to yourself) | `/roast @Alex` |
| `/quote` | Generate a fake-inspirational quote based on the conversation | `/quote` |

---

## 📁 Project Structure

```text
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
├── .github/workflows/      # GitHub Actions CI/CD workflows
├── Dockerfile              # Container definition for the bot
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (not committed)
```

---

## 🛠️ Tech Stack

- **[discord.py](https://discordpy.readthedocs.io/)** — Robust Discord API wrapper for Python
- **[Google Gemini](https://ai.google.dev/)** (`gemini-2.5-flash`) — Cutting-edge AI model for inference and text generation
- **[Docker](https://www.docker.com/)** — Containerization for seamless deployments
- **[GitHub Actions](https://github.com/features/actions)** — CI/CD for automated deployments

---

## ⚙️ Configuration

| Variable | Description |
|---|---|
| `DISCORD_TOKEN` | Your Discord bot token |
| `GEMINI_API_KEY` | Your Google Gemini API key |

> The AI model uses `gemini-2.5-flash` with a temperature of `0.7` and a max output of `2048` tokens. These can be easily adjusted within `services/ai_service.py`.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute as you see fit!
