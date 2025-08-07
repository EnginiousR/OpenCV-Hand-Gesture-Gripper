import cv2
import mediapipe as mp
import serial
import time

# Connect to Arduino (update COM port if needed)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

# Mediapipe hands setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

def is_fist(landmarks):
    # Fingers folded = fist
    return landmarks[8].y > landmarks[6].y and landmarks[12].y > landmarks[10].y

def is_open_palm(landmarks):
    # Fingers extended = open hand
    return landmarks[8].y < landmarks[6].y and landmarks[12].y < landmarks[10].y

last_state = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark

            if is_fist(lm) and last_state != 'fist':
                arduino.write(b'O')  # Fist now OPENS gripper
                last_state = 'fist'
                print(" Open (Fist Detected)")
            elif is_open_palm(lm) and last_state != 'open':
                arduino.write(b'G')  # Open hand now GRABS
                last_state = 'open'
                print(" Grab (Open Hand Detected)")

    cv2.imshow("Hand Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()
