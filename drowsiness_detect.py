import cv2
import pygame

# Initialize Pygame for the alarm sound
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound("alarm.wav")

# Load OpenCV's built-in Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
score = 0  # To track consecutive frames of closed eyes

while True:
    ret, frame = cap.read()
    height, width = frame.shape[:2]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale for speed

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25))

    # Default state: eyes are "closed" unless detected
    eyes_detected = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        
        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            eyes_detected = True
            cv2.rectangle(frame[y:y+h, x:x+w], (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    if not eyes_detected:
        score += 1 # Increment score if eyes are not found
        cv2.putText(frame, "Eyes Closed", (10, height-20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        
        # Trigger alarm if score exceeds 15 frames (0.5 seconds)
        if score > 15:
            try:
                alarm_sound.play()
            except:
                pass
            cv2.putText(frame, "DROWSINESS ALERT!", (width//4, height//2), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
    else:
        score = 0 # Reset score if eyes are detected
        alarm_sound.stop()
        cv2.putText(frame, "Eyes Open", (10, height-20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Driver Drowsiness Monitor', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
