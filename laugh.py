import sys
from naoqi import ALProxy

# Replace these with the actual IP address and port of your Nao robot
NAO_IP = "your_robot_ip_address"
NAO_PORT = 9559

def laugh():
    try:
        # Initialize the Naoqi audio player proxy
        audio_player = ALProxy("ALAudioPlayer", NAO_IP, NAO_PORT)

        # Replace with the path to your audio file on Nao's filesystem
        audio_file_path = "/path/to/your/audio/file.mp3"

        # Play the audio file
        audio_player.playFile(audio_file_path)

        print("Playing laugh audio.")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    laugh()
