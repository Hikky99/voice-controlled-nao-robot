import speech_recognition as sr
import subprocess
import sit
import stand
import laugh
import walk
import joke
import sing
import teach
import music

# Replace these with the actual IP address and port of your Nao robot
NAO_IP = "your_robot_ip_address"
NAO_PORT = 9559

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command recognized: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return None

def main():
    while True:
        command = listen_for_command()

        if command:
            if "sit" in command:
                sit.sit()
            elif "stand" in command:
                stand.stand()
            elif "laugh" in command:
                laugh.laugh()
            elif "walk" in command:
                walk.walk()
            elif "joke" in command:
                joke.joke()
            elif "sing" in command:
                sing.sing()
            elif "teach" in command:
                teach.teach()
            elif "play music" in command:
                music.play_music()
            else:
                print("Command not recognized. Please try again.")

if __name__ == "__main__":
    main()
