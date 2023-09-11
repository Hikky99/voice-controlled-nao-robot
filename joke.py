import random
from naoqi import ALProxy

# Replace these with the actual IP address and port of your Nao robot
NAO_IP = "your_robot_ip_address"
NAO_PORT = 9559

def joke():
    try:
        # Initialize the Naoqi text-to-speech proxy
        tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)

        # List of jokes
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
            "Parallel lines have so much in common. It's a shame they'll never meet.",
            "I used to play piano by ear, but now I use my hands.",
            "I'm reading a book on anti-gravity. It's impossible to put down!"
        ]

        # Choose a random joke
        random_joke = random.choice(jokes)

        # Have the robot speak the joke
        tts.say(random_joke)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    joke()
