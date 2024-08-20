# Spotify Discord webhook

This Python script allows you to create a Discord webhook that sends updates about the currently playing track on Spotify to a specified Discord channel.

## Setup
1. Install the required libraries by running:
   ```
   pip install spotipy aiohttp
   ```
2. Obtain the following credentials:
3. https://developer.spotify.com/
   - `CLIENT_ID`: Your Spotify client ID
   - `CLIENT_SECRET`: Your Spotify client secret
   - `REDIRECT_URI`: Your Spotify redirect URI
   - `WEBHOOK_URL`: Your Discord webhook URL

4. Update the script with your credentials in the designated placeholders.

## Usage
1. Run the script using:
   ```
   python spotify.py
   ```
2. The script will continuously check for the currently playing track on Spotify.
3. If a new track is detected, it will send a message to the specified Discord channel using the webhook URL.

## Note
- Make sure to set up the Discord webhook URL correctly to receive messages.
- The script runs an infinite loop checking every 30 seconds for updates.

Feel free to customize the script further based on your requirements!
