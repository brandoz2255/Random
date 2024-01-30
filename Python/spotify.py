import subprocess
import time

def open_spotify():
    # Adjust the command based on your Linux distribution and how Spotify is installed
    command = "spotify"
    subprocess.run(command, shell=True)
    print(f"Opened Spotify at {time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    # Set the time in 24-hour format (e.g., 08:00 for 8:00 AM)
    open_time = "08:05 PM"

    while True:
        current_time = time.strftime('%H:%M')
        if current_time == open_time:
            open_spotify()
            break
        else:
            # Sleep for a short duration and check again
            time.sleep(60)  # Check every minute until the specified time

