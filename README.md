# Voice-Controlled Nao Robot Application

<img src="assets/picture/hamza_nao.jpg" alt="Hamza with a Nao Robot" width="50%">

## Overview

This project involves building a voice-controlled application for a Nao robot. The application responds to specific voice commands by executing various actions. The primary components of the project include a `main.py` script that serves as the central control point and several modules that are called based on spoken commands.

## Project Details

- **Funding:** This project was made possible through generous funding from the Goethe Institut Ghana.

- **Project Description:** The project aims to demonstrate the capabilities of the Nao robot through natural language understanding and responsive actions.

- **Development Environment:** The programmed run on a Nao robot, which serves as the physical embodiment of the interactive application.

- **Resident Developer:** The project was undertaken by HamzaMohammed, who served as a resident developer at the Goethe Institut Ghana.

- **Acknowledgments:** The project received invaluable support from the Goethe Institut library team, particularly from the Head of Library and Information Service, Portia Eyram Meli Mansu, whose guidance and assistance were instrumental in its success.

## Script Descriptions

### `main.py`

- This script is the central control point of the application. It listens for voice commands and calls the corresponding modules to execute actions on the Nao robot.

### `sit.py`

- The `sit.py` module instructs the Nao robot to sit down when commanded.

### `stand.py`

- The `stand.py` module directs the Nao robot to stand up when given the relevant voice command.

### `laugh.py`

- The `laugh.py` module plays a humorous video ("laugh1.mp4") from the "assets" folder when the "laugh" command is spoken.

### `walk.py`

- The `walk.py` module orchestrates a sequence of actions when the "walk" command is heard:
  - If the robot is sitting, it stands up.
  - The robot starts walking.
  - It stops when it encounters an obstacle.
  - The robot turns around.
  - It returns to its initial position.

### `joke.py`

- The `joke.py` module tells a random joke when the "joke" command is received. It maintains a list of 5 different jokes.

### `sing.py`

- The `sing.py` module instructs the Nao robot to sing a song when commanded.

### `teach.py`

- The `teach.py` module enables the robot to:
  - Be commanded to teach.
  - Capture a taught phrase from the user.
  - Repeat the taught phrase to confirm learning.
  - Continuously teach random Ghanaian facts until the user commands it to stop. 

### `music.py`

- The `music.py` module plays a random audio music file from the "music" subfolder of the "assets" folder when executed. It utilizes Naoqi's `ALAudioPlayer` module for audio playback.

---

This project  demonstrates the potential for interactive applications of the Nao robot using natural language processing and responsive actions. It has been made possible through the support and collaboration with the Goethe Institut Ghana and its library team.
