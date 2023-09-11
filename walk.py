import sys
import time
from naoqi import ALProxy

# Replace these with the actual IP address and port of your Nao robot
NAO_IP = "your_robot_ip_address"
NAO_PORT = 9559

def walk():
    try:
        # Initialize the Naoqi motion proxy
        motion = ALProxy("ALMotion", NAO_IP, NAO_PORT)

        # Stand up if the robot is sitting
        motion.stand()

        # Get the initial position
        initial_position = motion.getRobotPosition(False)

        # Start walking forward
        motion.moveInit()
        motion.moveForward(0.5)  # Adjust the speed as needed

        while True:
            # Check for obstacles
            sonar_data = motion.sonar.getValue()
            if sonar_data[0] < 0.3:  # Detect obstacle within 30 cm
                print("Obstacle detected. Turning around and returning to initial position.")
                motion.stopMove()
                motion.moveTo(0.0, 0.0, 3.1416)  # Turn around (180 degrees)
                motion.moveInit()
                motion.moveTo(initial_position[0], initial_position[1], initial_position[2])  # Return to initial position
                motion.moveInit()
                motion.moveForward(0.5)  # Continue walking
            time.sleep(0.1)  # Check for obstacles every 0.1 seconds

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    walk()
