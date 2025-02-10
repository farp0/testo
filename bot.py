from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Replace these with your own values
api_id = 'YOUR_API_ID'  # Get from https://my.telegram.org/auth
api_hash = 'YOUR_API_HASH'  # Get from https://my.telegram.org/auth
bot_token = 'YOUR_BOT_TOKEN'  # Get from BotFather

# Create the Pyrogram client instance
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Handler for the /start command
@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply("Hello! I'm your bot. How can I assist you?")

# Handler for detecting when someone is typing
@app.on_chat_action()
async def typing_status(client, message: Message):
    if message.chat:
        if message.action == "typing":
            await message.reply("I see you're typing...")

# Handler for all incoming text messages
@app.on_message(filters.text)
async def echo(client, message: Message):
    # Echoes the text back to the user
    await message.reply(f"You said: {message.text}")

if __name__ == "__main__":
    app.run()
