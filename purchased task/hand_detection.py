import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

def detect_hand_landmarks():
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect hands and landmarks
        result = hands.process(rgb_frame)
        
        total_fingers = 0

        # Draw hand landmarks and count fingers
        if result.multi_hand_landmarks and result.multi_handedness:
            for hand_landmarks, handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
                hand_label = handedness.classification[0].label
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                # Count the number of fingers raised
                fingers_count = count_fingers(hand_landmarks, hand_label)
                total_fingers += fingers_count

            # Display the total finger count on the frame
            cv2.putText(frame, f'Total Fingers: {total_fingers}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Hand Landmark Detector', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()
    print(total_fingers)
    return total_fingers

def count_fingers(hand_landmarks, hand_label):
    # Tips of the fingers (thumb, index, middle, ring, pinky)
    finger_tips = [4, 8, 12, 16, 20]
    count = 0

    # Check if the fingers are raised
    for tip in finger_tips[1:]:  # Skip the thumb initially
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1

    # Special case for thumb: 
    # Compare x-coordinates if it's the left hand, and y-coordinates for the right hand
    if hand_label == 'Right':
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
            count += 1
    else:
        if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
            count += 1

    return count