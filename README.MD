# Chef Recipies Bot

This is a telegram bot built with Python, `aiogram`, `Mistral AI`.  
The bot allows user to get repice of any meal just by it's name/desc.

## Features

- Generate recipies for meal by its name or description
- Using free AI available everywhere (comparable to gpt-4o)

## Conditions

- Python 3.12 and above versions installed on your PC
- Bot Token. You can get it by creating a new bot [Telegram's BotFather](https://t.me/BotFather)
- AI API key. You can get if *for free* on [Mistral AI](https://mistral.ai/)

## Getting Started

1. **Clone this repository:**
   ```bash
   git clone https://github.com/JuicingNow/chef-ai-bot.git

2. **Install dependencies:**
    ```bash
    cd chef_bot
   pip install -r requirements.txt

3. **Create a `.env` file:**
   Create a `.env` file in the `app` directory.  
   This file will store your Telegram bot token and AI key. Open the `.env` file and add the following lines:<br>
   `TG_TOKEN="your-telegram-bot-token"`<br>
   `AI_TOKEN="your-ai-key"`


4. **Start the bot:**
    ```bash
    python run.py