from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Replace these with your own values
YOUR_API_ID = '3335796'  # Get from https://my.telegram.org/auth
YOUR_API_HASH = '138b992a0e672e8346d8439c3f42ea78'  # Get from https://my.telegram.org/auth
YOUR_BOT_TOKEN = '7136875110:AAF3hNDcTC4X2e9GQ7EePvOST7aTCPh1pGg'  # Get from BotFather
from pyrogram import Client, InlineKeyboardButton, InlineKeyboardMarkup

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual Pyrogram API credentials
app = Client("my_bot", api_id="YOUR_API_ID", api_hash="YOUR_API_HASH", bot_token="YOUR_BOT_TOKEN")

# Command to start the bot and send the inline keyboard
@app.on_message(filters.command("start"))
def start(client, message):
    # Create an inline keyboard with one button
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Visit GitHub", url="https://github.com/your-repo")]
        ]
    )
    # Send a message with the inline keyboard
    message.reply("Welcome to the bot! Here is your GitHub repository:", reply_markup=keyboard)

# Start the bot
app.run()
