from pyrogram import Client, filters
import time
# Replace these with your actual values
api_id = "3335796"
api_hash = "138b992a0e672e8346d8439c3f42ea78"
bot_token = "7136875110:AAF3hNDcTC4X2e9GQ7EePvOST7aTCPh1pGg"

# Initialize the bot client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
   # message.chat.send_action("typing")
   # time.sleep(2)
    message.reply("Hello! Welcome to the bot!")

# Handle the /help command
@app.on_message(filters.command("help"))
def help(client, message):
    
    message.chat.send_action("typing")
    time.sleep(2)
    message.reply("This is a bot that responds to /start and /help commands.")

# Handle any other message that starts with 
@app.on_message(filters.command("kir"))
def kir(client, message):
   message.chat.send_action("upload_photo")
   time.sleep(2)
   
    # Send a photo after the "typing" action
   message.reply_photo("https://example.com/path/to/your/image.jpg")

if __name__ == "__main__":
    app.run()
