import os
import random
from naoqi import ALProxy

# Replace these with the actual IP address and port of your Nao robot
NAO_IP = "your_robot_ip_address"
NAO_PORT = 9559

# Replace this with the actual path to the "assets/music" folder
MUSIC_FOLDER = "/path/to/assets/music"

def music():
    try:
        # Initialize the Naoqi audio player proxy
        audio_player = ALProxy("ALAudioPlayer", NAO_IP, NAO_PORT)

        # List all audio files in the "music" folder
        audio_files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith((".mp3", ".wav"))]

        if not audio_files:
            print("No music files found in the 'music' folder.")
            return

        # Select a random audio file
        random_music = random.choice(audio_files)

        # Set the path to the selected music file
        music_path = os.path.join(MUSIC_FOLDER, random_music)

        # Play the music file
        audio_player.playFile(music_path)

        print(f"Playing music: {random_music}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    music()
