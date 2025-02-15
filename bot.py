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
@app.on_message(filters.command("send_photo"))
def send_photo(client, message):
    client.send_photo(
        chat_id=message.chat.id,  # Send the photo to the chat where the command was received
        photo="photo.jpg",  # Replace with the path to your photo
        caption="Here is your requested photo!"  # Optional caption for the photo
    )

@app.on_message(filters.command("send_video"))
def send_video(client, message):
    client.send_video(
        chat_id=message.chat.id,  # Send the video to the chat where the command was received
        video="vid.mp4",  # Replace with the path to your video
        caption="Here is your requested video!"  # Optional caption for the video
)


if __name__ == "__main__":
    app.run()
