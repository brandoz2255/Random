

import os
import time

# Command to open Spotify
spotify_command = "spotify"

# Spotify URI for the playlist
playlist_uri = "37i9dQZF1E37JywefuQJE7"

# Command to play the playlist
playlist_command = f"spotify:playlist:{playlist_uri}"

# Command to set the volume to 80% (adjust as needed)
volume_command = "amixer -D pulse sset Master 80%"

# Open Spotify
os.system(spotify_command)

# Wait for Spotify to open (adjust the sleep time if needed)
time.sleep(5)

# Play the playlist
os.system(f"spotify --uri={playlist_command}")

# Set the volume
os.system(volume_command)
