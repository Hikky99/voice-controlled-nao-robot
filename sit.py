from naoqi import ALProxy

# Replace these with the actual IP address and port of your Nao robot
NAO_IP = "your_robot_ip_address"
NAO_PORT = 9559

def sit():
    try:
        # Initialize the Naoqi posture proxy
        posture = ALProxy("ALRobotPosture", NAO_IP, NAO_PORT)

        # Command the robot to sit down
        posture.goToPosture("Sit", 1.0)  # "Sit" is the predefined posture name

        print("Robot is sitting down.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    sit()
