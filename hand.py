import cv2 as cv
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Initialize webcam
cam = cv.VideoCapture(0)

# Initialize Mediapipe Hands module with proper parameters
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=2,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

while cam.isOpened():
    success, image = cam.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the image color from BGR to RGB
    image = cv.flip(image, 1)
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # Process the frame for hand detection
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
            )

    cv.imshow('Hand Tracker', image)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()

