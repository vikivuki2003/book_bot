📚 Book Bot

## 📝 Description

Book Bot is a Telegram bot designed for reading and managing books, specifically Ray Bradbury's "The Martian Chronicles." 
The bot allows users to navigate through the book, bookmark pages, and continue reading seamlessly. 
It provides a user-friendly interface for book lovers to enjoy literature directly from their Telegram app.

## ✨ Features

- 📖 Read "The Martian Chronicles" with easy navigation.
- 📑 Bookmark pages for quick access.
- ⏩ Continue reading from where you left off.
- 📜 View a list of bookmarks.
- 📚 User-friendly commands for easy interaction.

## 🛠 Technologies Used

- Python
- Aiogram (for Telegram Bot API)
- SQLite (for user data storage)
- HTML/CSS (for message formatting)

## 🚦 Requirements

- Python
- Aiogram
- SQLite

## 📦 Installation

1. Clone the repository:
   git clone https://github.com/vikivuki2003/book_bot.git
   cd book_bot
2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # For Unix
venv\Scripts\activate     # For Windows
3. Install the required packages:
pip install -r requirements.txt
Set up your Telegram bot:
4. Create a new bot using BotFather on Telegram.
Obtain your bot token.
Create a .env file in the root directory and add your bot token:
BOT_TOKEN=your_bot_token_here
5.Run the bot:
python main.py


🧪 Testing
To run tests, ensure you have a testing framework set up and execute:
pytest
