import sys
import os
import random
from naoqi import ALProxy

# Replace these with the actual IP address and port of your Nao robot
NAO_IP = "your_robot_ip_address"
NAO_PORT = 9559

# Replace this with the actual path to the "assets/songs" folder
SONGS_FOLDER = "assets/music"

def sing():
    try:
        # Initialize the Naoqi audio player proxy
        audio_player = ALProxy("ALAudioPlayer", NAO_IP, NAO_PORT)

        # List all audio files in the "songs" folder
        audio_files = [f for f in os.listdir(SONGS_FOLDER) if f.endswith((".mp3", ".wav"))]

        if not audio_files:
            print("I cant sing at this time.")
            return

        # Select a random audio file
        random_song = random.choice(audio_files)

        # Set the path to the selected song
        song_path = os.path.join(SONGS_FOLDER, random_song)

        # Play the audio file
        audio_player.playFile(song_path)

        print(f"Playing song: {random_song}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    sing()
