from naoqi import ALProxy

# Replace these with the actual IP address and port of your Nao robot
NAO_IP = "your_robot_ip_address"
NAO_PORT = 9559

def stand():
    try:
        # Initialize the Naoqi motion proxy
        motion = ALProxy("ALMotion", NAO_IP, NAO_PORT)

        # Command the robot to stand up
        motion.standInit(0.5)  # You can adjust the speed (0.5 in this example)

        print("Robot is standing up.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    stand()
