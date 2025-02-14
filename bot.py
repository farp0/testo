from pyrogram import Client, filters

# Replace these with your actual values
api_id = "3335796"
api_hash = "138b992a0e672e8346d8439c3f42ea78"
bot_token = "7136875110:AAF3hNDcTC4X2e9GQ7EePvOST7aTCPh1pGg"

# Initialize the bot client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    # Simulate typing
    await message.reply_chat_action("typing")  # Typing action
    time.sleep(2)  # Wait for 2 seconds while typing
    
    # Send a message after the typing effect
    await message.reply("Hello! I'm your bot. How can I help you today?")


if __name__ == "__main__":
    app.run()
