# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Telegram Bot API
ENV API_ID=your_api_id
ENV API_HASH=your_api_hash
ENV BOT_TOKEN=your_bot_token

# Expose the port (Optional, for HTTP servers, not necessary for bots)
EXPOSE 8080

# Run the bot script when the container starts
CMD ["python", "bot.py"]
