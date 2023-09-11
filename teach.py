import random
from naoqi import ALProxy
import speech_recognition as sr

# Replace these with the actual IP address and port of your Nao robot
NAO_IP = "your_robot_ip_address"
NAO_PORT = 9559

def teach():
    try:
        # Initialize the Naoqi text-to-speech proxy
        tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)

        # Initialize the speech recognition recognizer
        recognizer = sr.Recognizer()

        # List of Ghanaian facts
        ghanaian_facts = [
            "Ghana is known as the 'Gold Coast' because of its gold resources.",
            "Kente cloth, a colorful woven fabric, is a symbol of Ghanaian culture.",
            "Ghana is home to Lake Volta, one of the world's largest artificial lakes.",
            "The capital city of Ghana is Accra.",
            "Ghana was the first African country to gain independence from colonial rule in 1957.",
            "The Ashanti Empire was one of the powerful and influential kingdoms in Ghana's history.",
            "Ghana is famous for its cocoa production, making it one of the top cocoa producers globally.",
            "Ghanaian cuisine features dishes like jollof rice, fufu, and waakye.",
            "The Kwame Nkrumah Mausoleum in Accra is a memorial to Ghana's first president, Kwame Nkrumah.",
            "Ghana has a rich tradition of drumming and dance, including the popular dance form known as Azonto.",
            "The Kingdom of Dagbon is the oldest and one of the largest kingdoms in Ghana."
        ]

        while True:
            # Choose a random Ghanaian fact
            random_fact = random.choice(ghanaian_facts)

            # Have the robot speak the random fact
            tts.say(random_fact)

            # Listen for the user's command to stop
            with sr.Microphone() as source:
                audio = recognizer.listen(source)

                try:
                    # Recognize the speech
                    command = recognizer.recognize_google(audio).lower()

                    if "stop" in command:
                        print("Stopping the teaching.")
                        break

                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    print("Could not request results. Check your network connection.")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    teach()
