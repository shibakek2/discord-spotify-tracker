import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import aiohttp
import asyncio

CLIENT_ID = ''
CLIENT_SECRET = ''
WEBHOOK_URL = ''  # Add your Discord webhook URL here


def get_currently_playing():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                               client_secret=CLIENT_SECRET))
    current_track = sp.currently_playing()
    if current_track is not None and current_track['is_playing']:
        track = current_track['item']
        artist = track['artists'][0]['name']
        song = track['name']
        song_url = track['external_urls']['spotify']
        return f"Currently playing: {song} by {artist}", song_url

    else:
        return None, None


async def send_to_discord(song, song_url):
    async with aiohttp.ClientSession() as session:
        embed_data = {
            "embeds": [{
                "title": "Now Playing",
                "description": f"[{song}]({song_url})",
                "color": 0x1DB954  
            }]
        }
        async with session.post(WEBHOOK_URL, json=embed_data) as response:
            if response.status != 204:
                print(f"Failed to send message to Discord: {response.status}")


async def main():
    last_song = None
    while True:
        song, song_url = get_currently_playing()
        if song and song != last_song:
            await send_to_discord(song, song_url)
            last_song = song
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
