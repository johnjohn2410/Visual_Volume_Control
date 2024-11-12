# Visual Volume Control for ios

A Python application that allows you to control your Mac's volume using hand gestures detected via your webcam. This project leverages OpenCV and MediaPipe for real-time hand tracking and uses AppleScript to adjust the system volume on macOS.



## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- Real-time hand detection and tracking using MediaPipe.
- Gesture recognition to control system volume:
  - ** Increase volume** by moving your thumb and index finger apart.
  - ** Decrease volume** by bringing your thumb and index finger closer together.
- Visual feedback with OpenCV:
  - Displays webcam feed with overlays indicating detected landmarks.
  - Shows a volume bar and percentage on the screen.
- ** Supports using your iPhone as a webcam via Continuity Camera.**
- Cross-platform compatibility focused on **macOS**.



### Python Packages

- **OpenCV** (`opencv-python`)
- **MediaPipe** (`mediapipe`)
- **NumPy** (`numpy`)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/visual_volume_control.git
cd visual_volume_control
