#!/usr/bin/env python3
import os
import random
import time

def change_wallpaper(directory):
    wallpapers = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    if wallpapers:
        wallpaper_path = os.path.join(directory, random.choice(wallpapers))
        os.system(f"feh --bg-scale {wallpaper_path}")
        print(f"Changed wallpaper to {wallpaper_path}")
    else:
        print("No valid wallpapers found in the specified directory.")

if __name__ == "__main__":
    wallpaper_directory = "/path/to/your/wallpapers"
    while True:
        change_wallpaper(wallpaper_directory)
        # Change wallpaper every 10 minutes (adjust as needed)
        time.sleep(600)
