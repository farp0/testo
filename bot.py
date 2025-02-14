from pyrogram import Client, filters

# Replace these with your actual values
api_id = "3335796"
api_hash = "138b992a0e672e8346d8439c3f42ea78"
bot_token = "7136875110:AAF3hNDcTC4X2e9GQ7EePvOST7aTCPh1pGg"

# Initialize the bot client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Hello! I'm your Pyrogram bot!")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
