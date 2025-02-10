from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Replace these with your own values
api_id = '3335796'  # Get from https://my.telegram.org/auth
api_hash = '138b992a0e672e8346d8439c3f42ea78'  # Get from https://my.telegram.org/auth
bot_token = '7136875110:AAF3hNDcTC4X2e9GQ7EePvOST7aTCPh1pGg'  # Get from BotFather

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
