import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='google.protobuf.symbol_database')

import cv2
import mediapipe as mp
from math import hypot
import numpy as np
import subprocess

def set_volume_mac(volume):
    volume = int(volume)
    if 0 <= volume <= 100:
        subprocess.call(["osascript", "-e", f"set volume output volume {volume}"])
    else:
        print("Volume must be between 0 and 100")

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

volbar = 400
volper = 0

try:
    while True:
        success, img = cap.read()
        if not success:
            print("Failed to read frame from camera. Exiting...")
            break

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process hand landmarks
        results = hands.process(imgRGB)

        lmList = []
        if results.multi_hand_landmarks:
            for handlandmark in results.multi_hand_landmarks:
                for id, lm in enumerate(handlandmark.landmark):
                    h, w, _ = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

        if lmList != []:
            x1, y1 = lmList[4][1], lmList[4][2]   # Thumb tip
            x2, y2 = lmList[8][1], lmList[8][2]   # Index finger tip

            # Draw circles and line
            cv2.circle(img, (x1, y1), 13, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 13, (255, 0, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

            length = hypot(x2 - x1, y2 - y1)

            # Map hand range to volume range (0 to 100)
            vol = np.interp(length, [30, 350], [0, 100])
            volbar = np.interp(length, [30, 350], [400, 150])
            volper = np.interp(length, [30, 350], [0, 100])

            # Set volume
            set_volume_mac(vol)

            # Draw volume bar and percentage
            cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 4)
            cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, f"{int(volper)}%", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            print("Exiting program.")
            break

except KeyboardInterrupt:
    print("Program interrupted by user")

finally:
    cap.release()
    cv2.destroyAllWindows()
