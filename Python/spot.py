from spotify_local_control import SpotifyLocalControl

# Initialize the Spotify Local Control
slc = SpotifyLocalControl()

# Get the current playback status
status = slc.get_status()
print(status)

# Change the volume
slc.set_volume(100)

# Play a specific track
slc.play('spotify:track:your_track_id')

os.system(volume_command)
