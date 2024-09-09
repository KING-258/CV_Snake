# Created by [KING-258](https://www.github.com/KING-258), [D1NLonely](https://www.github.com/D1NLONELY) and [17Arhaan](https://www.github.com/17Arhaan)
## Overview

Welcome to the Nokia Snake Game! This classic game has been adapted with modern technology to provide an engaging and beneficial experience for individuals with autism. By leveraging OpenCV for movement detection, this version of Snake can help players develop and refine their motor skills while enjoying a nostalgic game.

## Features

- **Classic Nokia Snake Gameplay**: Enjoy the timeless Snake game experience, originally popularized on Nokia phones.
- **OpenCV Integration**: Use OpenCV for real-time movement detection, allowing for intuitive control of the snake.
- **Skill Development**: Designed to aid in the development of motor skills and hand-eye coordination.
- **Adaptive Difficulty**: The game dynamically adjusts its difficulty to match the player's skill level.

## Requirements

- Python 3.8 or above
- OpenCV
- Flask (for web integration)
- PyAutoGUI (for Automation)
- React (for frontend)
- Basic familiarity with Python and JavaScript

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/KING-258/CV_Snake.git
   cd CV_Snake

2. **Install Backend Dependencies**

   Navigate to the `backend` directory and install the required Python packages:

   ```bash
   pip install opencv-python
   pip install flask
   pip install flask-cors
   pip install pyautogui

## Usage

1. **Start the Backend**

   Navigate to the `backend` directory and run:

   ```bash
   cd server
   python3 app.py

2. **Start the Frontend**

   Navigate to the `frontend` directory and run:

   ```bash
   cd client
   npm start
   
3. **Play the Game**

   Open your browser and navigate to `http://localhost:3000` to start playing the game. The game will use your webcam feed to detect movement and control the snake.

## Controls

- **Movement**: Control the snake using actions done by the path of UV Light detected by OpenCV or use the arrows. 
- **Start/Pause**: Use the buttons in the game interface to start or pause the game.

## Development

- **Backend**: The backend is written in Python and uses OpenCV for movement detection. Modify `app.py` for backend changes.
- **Frontend**: The frontend is built with React. Modify `App.js` for frontend changes.

